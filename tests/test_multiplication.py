"""Pylint-clean tests for multiply()."""
from calculator import multiply


def test_multiply() -> None:
    """multiply returns correct product."""
    assert multiply(3, 4) == 12
