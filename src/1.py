import random

def solve_math_problem():
    operands = [1, 2, 3, 4, 5]
    operator = random.choice(["+", "-", "*", "/"])
    problem = f"{random.choice(operands)}{operator}{random.choice(operands)}"
    return eval(problem)