#!/usr/bin/env python3
import random

QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Return whether a number is even"""
    return num % 2 == 0


def game_challange():
    """Return the correct answer and question"""
    question = random.randint(1, 30)

    if is_even(question):
        answer = "yes"
    else:
        answer = "no"
    return question, answer
