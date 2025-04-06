# Mini Expression Evaluator in Python

import operator
import re

class ExpressionEvaluator:
    def __init__(self):
        self.vars = {}
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def evaluate(self, expr):
        expr = expr.replace(' ', '')
        tokens = re.findall(r'[a-zA-Z]+|\d+|[+\-*/()]', expr)
        output, ops = [], []

        def apply_op():
            b, a = output.pop(), output.pop()
            op = ops.pop()
            output.append(self.operators[op](a, b))

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                output.append(float(token))
            elif token.isalpha():
                output.append(self.vars.get(token, 0))
            elif token in self.operators:
                while (ops and ops[-1] in self.operators and
                       "+-".find(token) <= "+-".find(ops[-1])):
                    apply_op()
                ops.append(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops[-1] != '(':
                    apply_op()
                ops.pop()
            i += 1

        while ops:
            apply_op()

        return output[0]

    def assign(self, var, value):
        self.vars[var] = float(value)

# Usage
evaluator = ExpressionEvaluator()
evaluator.assign('x', 5)
evaluator.assign('y', 10)
print("Result:", evaluator.evaluate("3 + x * (2 + y)"))  # Expected: 63
