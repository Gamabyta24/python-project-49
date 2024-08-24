import math
import random

QUEST = "Find the greatest common divisor of given numbers."


def game_challange():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    true_answer = str(math.gcd(num1, num2))
    num = f"{num1} {num2}"
    return num, true_answer
