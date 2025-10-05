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

    def calculate(self, a, b, operator: str):
        if operator == '+':
            return self.add(a, b)
        elif operator == '-':
            return self.subtract(a, b)
        elif operator == '*':
            return self.multiply(a, b)
        elif operator in ['/', '÷']:
            return self.divide(a, b)
        else:
            raise ValueError("Unsupported operator")
