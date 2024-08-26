import random
from operator import add, sub, mul

QUEST = "What is the result of the expression?"


def game_challange():
    """Return the correct answer and question"""
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    operation_func, operation_symbol = choose_oper()
    answer = str(operation_func(num1, num2))
    question = f"{num1} {operation_symbol} {num2}"
    return question, answer


def choose_oper():
    """Return random func operator and str operator"""
    mass = [(add, "+"), (sub, "-"), (mul, "*")]
    return random.choice(mass)
