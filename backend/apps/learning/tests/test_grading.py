from apps.learning.grading import is_close, is_equivalent, normalize


def test_normalize_lowercases_and_strips_punctuation():
    assert normalize("  Hello, World!!  ") == "hello world"


def test_normalize_expands_contractions():
    assert normalize("I don't like it.") == "i do not like it"
    assert normalize("It's a test.") == normalize("It is a test.")


def test_normalize_handles_curly_apostrophes():
    assert normalize("she can’t swim") == "she can not swim"


def test_normalize_empty():
    assert normalize("") == ""


def test_is_equivalent_ignores_case_and_punctuation():
    assert is_equivalent("We Are Friends.", "we are friends") is True
    assert is_equivalent("I am fine", "I'm fine") is True
    assert is_equivalent("he is nice", "he was nice") is False


def test_is_close_accepts_small_typos():
    assert (
        is_close("There is a big park near my hous", "There is a big park near my house.") is True
    )
    assert is_close("completely different sentence", "There is a big park near my house.") is False


def test_is_close_empty_is_never_correct():
    assert is_close("", "There is a park.") is False
