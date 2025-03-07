import random

def get_random_math_problem(difficulty):
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        return f"{num1} + {num2}"
    elif difficulty == 2:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        return f"{num1} - {num2}"
    elif difficulty == 3:
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)
        return f"{num1} * {num2}"
    else:
        num1 = random.randint(1, 10000)
        num2 = random.randint(1, 10000)
        return f"{num1} / {num2}"
