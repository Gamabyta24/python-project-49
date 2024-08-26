import random

QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_challange():
    """Return the correct answer and question"""
    question = random.randint(1, 50)
    answer = "yes" if is_prime(question) else "no"
    return question, answer


def is_prime(num):
    """Return whether a number is prime"""
    return num > 1 and all(num % i for i in range(2, int(num**0.5) + 1))
