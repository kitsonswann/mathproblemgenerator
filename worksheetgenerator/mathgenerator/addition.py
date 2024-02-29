import random

def generate_addition_problem(max_digit=9, max_answer=10, min_digit=1, min_answer=2):

    if max_answer <= max_digit:
        raise Exception('Max answer must be bigger than max digit.')

    first_digit = random.randint(min_digit, max_digit)
    second_answer_range = max_answer-first_digit
    second_digit = random.randint(min_digit, second_answer_range)

    return first_digit, second_digit, (first_digit+second_digit)