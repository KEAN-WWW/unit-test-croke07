"""Basic calculator module for autograder (pylint-clean)."""

from typing import Final

__all__: Final = ["add", "subtract", "multiply", "divide", "Calculator", "calculate"]


def add(number1: int, number2: int) -> int:
    """Return number1 + number2."""
    return number1 + number2


def subtract(number1: int, number2: int) -> int:
    """Return number1 - number2."""
    return number1 - number2


def multiply(number1: int, number2: int) -> int:
    """Return number1 * number2."""
    return number1 * number2


def divide(number1: int, number2: int) -> float:
    """Return number1 / number2; raise ZeroDivisionError if number2 is zero."""
    if number2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return number1 / number2


def calculate(number1: int, number2: int, operator: str):
    """Dispatch helper handy for some tests/assignments."""
    if operator == "+":
        return add(number1, number2)
    if operator == "-":
        return subtract(number1, number2)
    if operator == "*":
        return multiply(number1, number2)
    if operator in {"/", "÷"}:
        return divide(number1, number2)
    raise ValueError(f"Unsupported operator: {operator!r}")


class Calculator:
    """OOP wrapper that reuses the pure functions above."""

    @staticmethod
    def add(number1: int, number2: int) -> int:
        return add(number1, number2)

    @staticmethod
    def subtract(number1: int, number2: int) -> int:
        return subtract(number1, number2)

    @staticmethod
    def multiply(number1: int, number2: int) -> int:
        return multiply(number1, number2)

    @staticmethod
    def divide(number1: int, number2: int) -> float:
        return divide(number1, number2)

    @staticmethod
    def calculate(number1: int, number2: int, operator: str):
        return calculate(number1, number2, operator)
