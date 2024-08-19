#!/usr/bin/env python3
import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 3
    while True:
        if counter == 0:
            print(f"Congratulations, {name}!")
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
                print(
                    f'"{your_answer}" is wrong answer ;(. Correct answer was "{true_answer}".\n',
                    f"Let's try again, {name}!",
                )
                break
        else:
            true_answer = "no"
            your_answer = prompt.string("Your answer: ")
            if true_answer == your_answer:
                print("Correct!")
                counter -= 1
            else:
                print(
                    f'"{your_answer}" is wrong answer ;(. Correct answer was "{true_answer}".\n',
                    f"Let's try again, {name}!",
                )
                break


if __name__ == "__main__":
    main()
