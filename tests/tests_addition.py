"""Pylint-clean tests for add()."""
from calculator import add


def test_add() -> None:
    """add returns correct sum."""
    assert add(2, 3) == 5
