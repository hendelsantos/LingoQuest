"""Currículo LingoQuest organizado por nível CEFR (A1 a C2).

Cada módulo deste pacote define ``COURSE`` (metadados do curso) e ``UNITS``
(estrutura de unidades, lições e perguntas). A importação é preguiçosa para
que módulos ainda não escritos não quebrem o carregamento.
"""

from importlib import import_module

LEVEL_MODULES = ("a1", "a2", "b1", "b2", "c1", "c2")


def load_catalog() -> list[tuple[dict, list]]:
    """Retorna uma lista de tuplas ``(course, units)`` na ordem dos níveis."""
    catalog: list[tuple[dict, list]] = []
    for name in LEVEL_MODULES:
        module = import_module(f".{name}", package=__name__)
        catalog.append((module.COURSE, module.UNITS))
    return catalog
