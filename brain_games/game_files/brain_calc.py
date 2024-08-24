import random
from operator import add, sub, mul

QUEST = "What is the result of the expression?"


def game_challange():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    x, y = choose_oper()
    true_answer = str(x(num1, num2))
    num = f"{num1} {y} {num2}"
    return num, true_answer


def choose_oper():
    mass = [(add, "+"), (sub, "-"), (mul, "*")]
    return random.choice(mass)
