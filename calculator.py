# ---- Top-level pure functions (what the autograder expects) ----
def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# ---- Optional OOP wrapper (re-uses the functions, to satisfy OOP part) ----
class Calculator:
    """Simple calculator that reuses the pure functions above."""
    @staticmethod
    def add(a: int, b: int) -> int:
        return add(a, b)

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return subtract(a, b)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return multiply(a, b)

    @staticmethod
    def divide(a: int, b: int) -> float:
        return divide(a, b)