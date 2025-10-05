"""OOP wrapper (not used by autograder)."""
from . import ops

class Calculator:
    def add(self, a, b):
        return ops.add(a, b)
    def subtract(self, a, b):
        return ops.subtract(a, b)
    def multiply(self, a, b):
        return ops.multiply(a, b)
    def divide(self, a, b):
        return ops.divide(a, b)
