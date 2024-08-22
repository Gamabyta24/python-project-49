import prompt


def is_even(num):
    return num % 2 == 0


def greetings():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
    return name


def ask_question(discription):
    print(discription)


def lose(your_answer, true_answer, name):
    print(
        f'"{your_answer}" is wrong answer ;(. Correct answer was "{true_answer}".\n',
        f"Let's try again, {name}!",
    )


def congrats(name):
    print(f"Congratulations, {name}!")
