import prompt
from brain_games.module import greetings, lose, congrats


def run_game_engine(game_module):
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
