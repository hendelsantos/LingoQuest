"""Validador estrutural do conteúdo do currículo.

Uso (a partir do diretório ``backend``)::

    .venv/bin/python -m apps.learning.content.validate          # todos os níveis
    .venv/bin/python -m apps.learning.content.validate a2 b1    # níveis específicos

Erros encerram com código 1; avisos (warnings) são apenas recomendações
pedagógicas. Não requer Django nem banco de dados.
"""

import importlib
import re
import sys

ALLOWED_SKILLS = {
    "Grammar",
    "Vocabulary",
    "Conversation",
    "Listening",
    "Speaking",
    "Review",
    "Writing",
}
QUESTION_TYPES = {"MCQ", "FILL_IN", "ORDERING", "LISTENING"}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

MIN_THEORY_CHARS = 80
SUMMARY_MAX = 240
PROMPT_MAX = 300
EXPLANATION_MAX = 300


def check_pedagogy(report: "Report", path: str, pedagogy: object) -> None:
    if pedagogy is None:
        return
    if not isinstance(pedagogy, dict):
        report.error(f"{path}.pedagogy deve ser um dicionário.")
        return

    for key in ("objective", "activation_prompt"):
        value = pedagogy.get(key)
        if not isinstance(value, str) or not value.strip():
            report.error(f"{path}.pedagogy.{key} é obrigatório.")

    for key, minimum, maximum in (
        ("common_mistakes", 2, 4),
        ("review_prompts", 2, 4),
    ):
        values = pedagogy.get(key)
        if not isinstance(values, list) or not minimum <= len(values) <= maximum:
            report.error(
                f"{path}.pedagogy.{key} exige de {minimum} a {maximum} itens."
            )
        elif any(not isinstance(value, str) or not value.strip() for value in values):
            report.error(f"{path}.pedagogy.{key} deve conter apenas textos não vazios.")

    task = pedagogy.get("production_task")
    if not isinstance(task, dict):
        report.error(f"{path}.pedagogy.production_task deve ser um dicionário.")
        return
    if task.get("mode") not in {"SPEAKING", "WRITING"}:
        report.error(
            f"{path}.pedagogy.production_task.mode deve ser SPEAKING ou WRITING."
        )
    for key in ("prompt", "model"):
        value = task.get(key)
        if not isinstance(value, str) or not value.strip():
            report.error(f"{path}.pedagogy.production_task.{key} é obrigatório.")
    checklist = task.get("checklist")
    if not isinstance(checklist, list) or not 2 <= len(checklist) <= 5:
        report.error(
            f"{path}.pedagogy.production_task.checklist exige de 2 a 5 itens."
        )
    elif any(not isinstance(value, str) or not value.strip() for value in checklist):
        report.error(
            f"{path}.pedagogy.production_task.checklist deve conter textos não vazios."
        )


class Report:
    def __init__(self, label: str) -> None:
        self.label = label
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def ok(self) -> bool:
        return not self.errors

    def summary(self) -> str:
        lessons = self.lessons
        questions = self.questions
        lines = [
            f"{self.label}: {self.units} unidades, {lessons} lições, {questions} perguntas"
        ]
        lines += [f"  AVISO: {item}" for item in self.warnings]
        lines += [f"  ERRO: {item}" for item in self.errors]
        return "\n".join(lines)

    units = 0
    lessons = 0
    questions = 0


def check_course(report: Report, course: dict, level: str) -> None:
    for key in ("slug", "title", "description", "level"):
        if not course.get(key):
            report.error(f"COURSE.{key} é obrigatório e não pode ser vazio.")
    slug = course.get("slug", "")
    if not KEBAB.match(slug or ""):
        report.error(f"slug de curso inválido: {slug!r}")
    if level != "a1" and not slug.startswith(f"{level}-"):
        report.error(f"slug de curso {slug!r} deve começar com {level!r}-.")
    if course.get("level") != level.upper():
        report.error(f"COURSE.level deve ser {level.upper()}.")


def check_question(report: Report, path: str, question: dict) -> None:
    qtype = question.get("type")
    if qtype not in QUESTION_TYPES:
        report.error(f"{path}: tipo de pergunta inválido: {qtype!r}")
        return
    prompt = question.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        report.error(f"{path}.prompt é obrigatório.")
    elif len(prompt) > PROMPT_MAX:
        report.error(f"{path}.prompt excede {PROMPT_MAX} caracteres.")
    explanation = question.get("explanation")
    if not isinstance(explanation, str) or not explanation.strip():
        report.error(f"{path}.explanation é obrigatória (feedback pedagógico).")
    elif len(explanation) > EXPLANATION_MAX:
        report.error(f"{path}.explanation excede {EXPLANATION_MAX} caracteres.")

    if qtype == "MCQ":
        choices = question.get("choices")
        if not isinstance(choices, list) or not 3 <= len(choices) <= 5:
            report.error(f"{path}: MCQ exige de 3 a 5 alternativas.")
            return
        if any(not isinstance(choice, str) or not choice.strip() for choice in choices):
            report.error(f"{path}: alternativas devem ser textos não vazios.")
        if len(set(choices)) != len(choices):
            report.warn(f"{path}: alternativas repetidas.")
        index = question.get("correct_index")
        if not isinstance(index, int) or not 0 <= index < len(choices):
            report.error(f"{path}.correct_index fora do intervalo das alternativas.")
    else:
        correct = question.get("correct")
        if not isinstance(correct, str) or not correct.strip():
            report.error(f"{path}.correct é obrigatório para o tipo {qtype}.")
            return
        words = correct.split()
        if qtype in {"ORDERING", "LISTENING"} and not 3 <= len(words) <= 12:
            report.error(f"{path}: {qtype} exige frases de 3 a 12 palavras.")
        if qtype == "ORDERING" and correct.strip()[-1] not in ".?!":
            report.error(f"{path}: ORDERING deve terminar com pontuação final.")
        if qtype == "FILL_IN" and len(correct) > 40:
            report.error(f"{path}: FILL_IN aceita no máximo 40 caracteres.")
        accepted = question.get("accepted")
        if accepted is not None:
            if not isinstance(accepted, list) or not accepted:
                report.error(f"{path}.accepted deve ser uma lista não vazia quando presente.")
            elif any(not isinstance(item, str) or not item.strip() for item in accepted):
                report.error(f"{path}.accepted deve conter apenas textos não vazios.")
            elif correct not in accepted:
                report.error(f"{path}.accepted deve incluir a resposta principal correct.")
        if qtype == "FILL_IN" and "___" not in (prompt or ""):
            report.warn(f"{path}: FILL_IN costuma indicar a lacuna com ___ no prompt.")


def check_lesson(
    report: Report,
    path: str,
    lesson: dict,
    level: str,
    seen_slugs: dict[str, str],
) -> None:
    slug = lesson.get("slug", "")
    if not KEBAB.match(slug or ""):
        report.error(f"{path}.slug inválido: {slug!r}")
    if slug in seen_slugs:
        report.error(f"slug de lição duplicado: {slug!r} (também em {seen_slugs[slug]}) — slugs devem ser únicos globalmente.")
    else:
        seen_slugs[slug] = path
    if level != "a1" and not slug.startswith(f"{level}-"):
        report.error(f"{path}.slug deve começar com {level!r}-: {slug!r}")

    title = lesson.get("title")
    if not isinstance(title, str) or not title.strip() or len(title) > 160:
        report.error(f"{path}.title é obrigatório (até 160 caracteres).")
    skill = lesson.get("skill")
    if skill not in ALLOWED_SKILLS:
        report.error(f"{path}.skill inválido: {skill!r} (use um de {sorted(ALLOWED_SKILLS)}).")
    summary = lesson.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        report.error(f"{path}.summary é obrigatório.")
    elif len(summary) > SUMMARY_MAX:
        report.error(f"{path}.summary excede {SUMMARY_MAX} caracteres.")
    theory = lesson.get("theory")
    if not isinstance(theory, str) or len(theory.strip()) < MIN_THEORY_CHARS:
        report.error(f"{path}.theory muito curta (mínimo {MIN_THEORY_CHARS} caracteres).")
    example = lesson.get("example")
    if not isinstance(example, str) or not example.strip():
        report.error(f"{path}.example é obrigatório (exemplo em inglês).")
    key_points = lesson.get("key_points")
    if not isinstance(key_points, list) or not 3 <= len(key_points) <= 6:
        report.error(f"{path}.key_points exige de 3 a 6 itens.")
    elif any(not isinstance(point, str) or not point.strip() for point in key_points):
        report.error(f"{path}.key_points deve conter apenas textos não vazios.")

    check_pedagogy(report, path, lesson.get("pedagogy"))

    dialogue = lesson.get("dialogue")
    if dialogue is not None:
        if not isinstance(dialogue, list) or not 4 <= len(dialogue) <= 12:
            report.error(f"{path}.dialogue deve ter de 4 a 12 falas.")
        else:
            for index, line in enumerate(dialogue, start=1):
                if not isinstance(line, dict):
                    report.error(f"{path}.dialogue[{index}] deve ser um dicionário.")
                    continue
                speaker = line.get("speaker")
                text = line.get("line")
                if not isinstance(speaker, str) or not speaker.strip():
                    report.error(f"{path}.dialogue[{index}].speaker é obrigatório.")
                if not isinstance(text, str) or not text.strip():
                    report.error(f"{path}.dialogue[{index}].line é obrigatória.")
        if skill not in {"Conversation", "Speaking"}:
            report.warn(f"{path}: dialogue costuma aparecer em lições de Conversation.")

    questions = lesson.get("questions")
    if not isinstance(questions, list) or not 4 <= len(questions) <= 6:
        report.error(f"{path}: cada lição exige de 4 a 6 perguntas.")
        return
    types = {question.get("type") for question in questions if isinstance(question, dict)}
    if len(types) < 2:
        report.warn(f"{path}: use pelo menos 2 tipos de exercício diferentes na lição.")
    if "LISTENING" not in types:
        report.warn(f"{path}: inclua pelo menos um ditado (LISTENING) por lição.")
    for index, question in enumerate(questions, start=1):
        if not isinstance(question, dict):
            report.error(f"{path}.questions[{index}] deve ser um dicionário.")
            continue
        check_question(report, f"{path}.questions[{index}]", question)
        report.questions += 1


def check_module(level: str, seen_slugs: dict[str, str]) -> Report:
    report = Report(level.upper())
    try:
        module = importlib.import_module(f"apps.learning.content.{level}")
    except (ImportError, SyntaxError) as exc:  # noqa: PERF203
        report.error(f"não foi possível importar o módulo: {exc}")
        return report

    course = getattr(module, "COURSE", None)
    units = getattr(module, "UNITS", None)
    if not isinstance(course, dict):
        report.error("COURSE deve ser um dicionário.")
        return report
    if not isinstance(units, list) or not 3 <= len(units) <= 7:
        report.error("UNITS deve ser uma lista com 3 a 7 unidades.")
        return report

    check_course(report, course, level)

    positions = [unit.get("position") for unit in units]
    if sorted(position for position in positions if isinstance(position, int)) != list(
        range(1, len(units) + 1)
    ):
        report.error(f"posições de unidades devem ser 1..{len(units)} sem repetições.")

    for unit_index, unit in enumerate(units, start=1):
        if not isinstance(unit, dict):
            report.error(f"UNITS[{unit_index}] deve ser um dicionário.")
            continue
        path = f"UNITS[{unit_index}]"
        for key in ("title", "position", "description"):
            if unit.get(key) in (None, ""):
                report.error(f"{path}.{key} é obrigatório.")
        lessons = unit.get("lessons")
        if not isinstance(lessons, list) or not 3 <= len(lessons) <= 6:
            report.error(f"{path}: cada unidade exige de 3 a 6 lições.")
            continue
        report.units += 1
        for lesson_index, lesson in enumerate(lessons, start=1):
            if not isinstance(lesson, dict):
                report.error(f"{path}.lessons[{lesson_index}] deve ser um dicionário.")
                continue
            check_lesson(
                report,
                f"{path}.lessons[{lesson_index}]",
                lesson,
                level,
                seen_slugs,
            )
            report.lessons += 1

    conversation_lessons = sum(
        1
        for unit in units
        if isinstance(unit, dict)
        for lesson in unit.get("lessons", [])
        if isinstance(lesson, dict) and lesson.get("skill") == "Conversation"
    )
    if conversation_lessons == 0:
        report.warn("nenhuma lição de Conversation no nível (recomendado ao menos 3).")

    review_lessons = sum(
        1
        for unit in units
        if isinstance(unit, dict)
        for lesson in unit.get("lessons", [])
        if isinstance(lesson, dict) and lesson.get("skill") == "Review"
    )
    if review_lessons == 0:
        report.warn("nenhuma lição de Review no nível (recomendado ao menos 1).")

    return report


def main(argv: list[str]) -> int:
    levels = argv[1:] or ["a1", "a2", "b1", "b2", "c1", "c2"]
    seen_slugs: dict[str, str] = {}
    reports = []
    for level in levels:
        reports.append(check_module(level, seen_slugs))

    print()
    for report in reports:
        print(report.summary())
    print()

    failed = [report.label for report in reports if not report.ok()]
    if failed:
        print(f"VALIDAÇÃO FALHOU para: {', '.join(failed)}")
        return 1
    if len(reports) > 1:
        total_lessons = sum(report.lessons for report in reports)
        total_questions = sum(report.questions for report in reports)
        print(
            f"Conteúdo válido: {len(reports)} níveis, "
            f"{total_lessons} lições e {total_questions} perguntas."
        )
    else:
        print("Conteúdo válido.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
