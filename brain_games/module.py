import prompt


def is_even(num):
    return num % 2 == 0


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(discription):
    print(discription)


def lose(your, true_a, name):
    print(
        f'"{your}" is wrong answer ;(. Correct answer was "{true_a}".\n',
        f"Let's try again, {name}!",
    )


def congrats(name):
    print(f"Congratulations, {name}!")
