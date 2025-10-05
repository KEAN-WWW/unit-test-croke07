import pytest
from calculator.calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.add(1, 2) == 3

def test_subtract():
    assert calc.subtract(4, 2) == 2

def test_multiply():
    assert calc.multiply(3, 3) == 9

def test_divide():
    assert calc.divide(8, 2) == 4.0

def test_invalid_operator():
    with pytest.raises(ValueError):
        calc.calculate(2, 3, '%')
