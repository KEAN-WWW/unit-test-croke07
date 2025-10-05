"""Pylint-clean tests for divide()."""
import pytest
from calculator import divide


def test_divide() -> None:
    """divide returns correct quotient."""
    assert divide(6, 3) == 2.0


def test_divide_zero_exception() -> None:
    """divide raises on zero divisor."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
