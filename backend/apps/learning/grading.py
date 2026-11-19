"""Correção de respostas no servidor, com normalização de texto.

A normalização torna equivalentes variações irrelevantes de escrita:
maiúsculas, pontuação, espaços extras, apóstrofos curvos e contrações
("don't" == "do not"). Ditados (LISTENING) aceitam, além disso, pequenos
erros de digitação via similaridade de sequências.
"""

import re
import unicodedata
from difflib import SequenceMatcher

from .models import Question

LISTENING_SIMILARITY_THRESHOLD = 0.85

_APOSTROPHES = {"’": "'", "‘": "'", "ʼ": "'", "`": "'"}

# Expande contrações para que "it is" e "it's" sejam tratadas como iguais.
_CONTRACTIONS = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "can not",
    "cannt": "can not",
    "cannot": "can not",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "here's": "here is",
    "how's": "how is",
    "i'd": "i would",
    "i'll": "i will",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'll": "it will",
    "it's": "it is",
    "let's": "let us",
    "mightn't": "might not",
    "mustn't": "must not",
    "shan't": "shall not",
    "she'd": "she would",
    "she'll": "she will",
    "she's": "she is",
    "shouldn't": "should not",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'll": "we will",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what's": "what is",
    "where's": "where is",
    "who's": "who is",
    "won't": "will not",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have",
}


def normalize(text: str) -> str:
    """Reduz o texto a uma sequência comparável de palavras."""
    if not text:
        return ""
    value = unicodedata.normalize("NFKC", text).strip().lower()
    for source, target in _APOSTROPHES.items():
        value = value.replace(source, target)
    # Mantém letras, números, apóstrofo (possessivos) e espaços.
    value = re.sub(r"[^a-z0-9'\s]", " ", value)
    tokens = [_CONTRACTIONS.get(token, token) for token in value.split()]
    return " ".join(tokens)


def is_equivalent(candidate: str, target: str) -> bool:
    """Comparação exata após normalização (para gramática e ordenação)."""
    return bool(candidate) and normalize(candidate) == normalize(target)


def similarity(candidate: str, target: str) -> float:
    return SequenceMatcher(None, normalize(candidate), normalize(target)).ratio()


def is_close(
    candidate: str, target: str, threshold: float = LISTENING_SIMILARITY_THRESHOLD
) -> bool:
    """Comparação tolerante para ditados: aceita pequenos erros de digitação."""
    if not candidate:
        return False
    if is_equivalent(candidate, target):
        return True
    return similarity(candidate, target) >= threshold


class InvalidAnswer(Exception):
    code = "INVALID_ANSWER"
    detail = "Envie uma resposta válida."

    def __init__(self, *, code: str | None = None, detail: str | None = None) -> None:
        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        super().__init__(self.detail)


def grade_answer(question: Question, data: dict) -> dict:
    """Compara a resposta enviada com o gabarito, conforme o tipo da questão."""
    explanation = question.explanation

    if question.type == Question.Type.MCQ:
        selected = next(
            (choice for choice in question.choices.all() if choice.id == data["choiceId"]),
            None,
        )
        if selected is None:
            raise InvalidAnswer(code="CHOICE_NOT_AVAILABLE", detail="Alternativa inválida.")
        correct = next(choice for choice in question.choices.all() if choice.is_correct)
        return {
            "isCorrect": selected.is_correct,
            "selectedChoiceId": selected.id,
            "correctChoiceId": correct.id,
            "explanation": explanation,
        }

    correct = str(question.answer_data.get("correct", "")).strip()
    if not correct:
        raise InvalidAnswer()

    if question.type == Question.Type.ORDERING:
        order = data.get("order")
        if not isinstance(order, list) or not order:
            raise InvalidAnswer(detail="Organize as palavras antes de confirmar.")
        answer = " ".join(str(token).strip() for token in order if str(token).strip())
        return {
            "isCorrect": is_equivalent(answer, correct),
            "correctAnswer": correct,
            "explanation": explanation,
        }

    answer = data.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise InvalidAnswer()

    if question.type == Question.Type.LISTENING:
        return {
            "isCorrect": is_close(answer, correct),
            "correctAnswer": correct,
            "explanation": explanation,
        }

    accepted = question.answer_data.get("accepted") or [correct]
    is_correct = any(is_equivalent(candidate, answer) for candidate in accepted)
    return {"isCorrect": is_correct, "correctAnswer": correct, "explanation": explanation}


def error_category(question: Question, data: dict) -> str:
    if question.type == Question.Type.LISTENING:
        return "LISTENING"
    if question.type == Question.Type.ORDERING:
        return "WORD_ORDER"
    if question.type == Question.Type.FILL_IN:
        answer = data.get("answer")
        correct = str(question.answer_data.get("correct", ""))
        if isinstance(answer, str) and correct and similarity(answer, correct) >= 0.9:
            return "SPELLING"
    if question.lesson.skill == "Vocabulary":
        return "VOCABULARY"
    if question.lesson.skill in {"Conversation", "Speaking", "Review"}:
        return "COMPREHENSION"
    return "GRAMMAR"
