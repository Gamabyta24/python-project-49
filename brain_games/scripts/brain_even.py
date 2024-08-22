#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.module import greetings, lose, congrats


def is_even(num):
    return num % 2 == 0


def main():
    name = greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 3
    while True:
        if counter == 0:
            congrats(name)
            break
        quest_number = random.randint(1, 15)
        print("question:", quest_number)
        if quest_number % 2 == 0:
            true_answer = "yes"
            your_answer = prompt.string("Your answer: ")
            if true_answer == your_answer:
                print("Correct!")
                counter -= 1
            else:
                lose(your_answer, true_answer, name)
                break
        else:
            true_answer = "no"
            your_answer = prompt.string("Your answer: ")
            if true_answer == your_answer:
                print("Correct!")
                counter -= 1
            else:
                lose(your_answer, true_answer, name)
                break


if __name__ == "__main__":
    main()
