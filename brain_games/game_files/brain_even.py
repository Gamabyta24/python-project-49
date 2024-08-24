#!/usr/bin/env python3
import prompt
import random

QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def game_challange():
    num = random.randint(1, 30)

    if num % 2 == 0:
        true_answer = "yes"
    else:
        true_answer = "no"
    return num, true_answer
