"""Pylint-clean tests for subtract()."""
from calculator import subtract


def test_subtract() -> None:
    """subtract returns correct difference."""
    assert subtract(5, 2) == 3
