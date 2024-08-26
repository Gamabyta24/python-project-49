import prompt


def run_game_engine(game_module):
    """function that launches the game module"""
    player_name = greetings()
    print(game_module.QUEST)
    for _ in range(3):
        question, true_answer = game_module.game_challange()
        print("Question:", question)
        player_answer = prompt.string("Your answer: ")
        if player_answer == true_answer:
            print("Correct!")
        else:
            lose(player_answer, true_answer, player_name)
            return
    congrats(player_name)

def greetings():
    """function that welcomes the user"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def ask_question(discription):
    """function that shows the task"""
    print(discription)


def lose(your, true_a, name):
    """function that notifies about defeat"""
    print(
        f'"{your}" is wrong answer ;(. Correct answer was "{true_a}".\n',
        f"Let's try again, {name}!",
    )


def congrats(name):
    """function that congratulates you on your victory"""
    print(f"Congratulations, {name}!")
