import random

def get_random_math_problem(max_value=10):
    """
    Returns a random math problem with two variables x and y,
    where x and y are integers between 1 and max_value (inclusive).
    The problem consists of one of the four operations: addition, subtraction, multiplication or division.
    """
    operation = random.choice(["+", "-", "*", "/"])
    x = random.randint(1, max_value)
    y = random.randint(1, max_value)
    if operation == "+":
        return f"{x} {operation} {y}"
    elif operation == "-":
        return f"{x} - {y}"
    elif operation == "*":
        return f"{x} * {y}"
    else:
        return f"{x} / {y}"
