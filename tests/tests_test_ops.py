import pytest

import calculator as ops

def test_add():
    assert ops.add(2, 3) == 5

def test_subtract():
    assert ops.subtract(5, 2) == 3

def test_multiply():
    assert ops.multiply(3, 4) == 12

def test_divide():
    assert ops.divide(6, 3) == 2.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        ops.divide(4, 0)
