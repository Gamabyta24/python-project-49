from brain_games.scripts.module import greetings, lose, congrats
import prompt
from operator import add, mul, sub
from random import randint, choice


def choose_oper():
    mass = [(add, "+"), (sub, "-"), (mul, "*")]
    return choice(mass)


def main():
    name = greetings()
    print("What is the result of the expression?")
    for _ in range(3):
        num1 = randint(1, 30)
        num2 = randint(1, 30)
        x, y = choose_oper()
        print("Question:", num1, y, num2)
        true_answer = str(x(num1, num2))
        your_answer = prompt.string("Your answer: ")
        if true_answer == your_answer:
            print("Correct!")
            continue
        else:
            lose(your_answer, true_answer, name)
            return
    congrats(name)


if __name__ == "__main__":
    main()
