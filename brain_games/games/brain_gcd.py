import math
import random

QUEST = "Find the greatest common divisor of given numbers."


def game_challange():
    """Return the correct answer and question"""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = str(math.gcd(num1, num2))
    question = f"{num1} {num2}"
    return question, answer
