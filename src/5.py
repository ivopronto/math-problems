def get_random_math_problem(level=1):
    if level == 1:
        return "print('Please enter your answer to the following math problem: 2 + 2')"
    elif level == 2:
        return "print('Please enter your answer to the following math problem: 5 * 5')"
    elif level == 3:
        return "print('Please enter your answer to the following math problem: 7 - 3')"
    else:
        return "print('Please enter your answer to the following math problem: 9 / 3')"
