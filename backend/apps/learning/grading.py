"""Correção de respostas no servidor, com normalização de texto.

A normalização torna equivalentes variações irrelevantes de escrita:
maiúsculas, pontuação, espaços extras, apóstrofos curvos e contrações
("don't" == "do not"). Ditados (LISTENING) aceitam, além disso, pequenos
erros de digitação via similaridade de sequências.
"""

import re
import unicodedata
from difflib import SequenceMatcher

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
