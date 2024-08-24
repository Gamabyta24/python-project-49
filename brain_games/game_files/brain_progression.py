import random

QUEST = "What number is missing in the progression?"


def game_challange():
    progression = []
    num_start = random.randint(1, 15)
    num_step = random.randint(1, 15)
    for _ in range(10):
        progression.append(num_start)
        num_start = num_start + num_step
    true_answer = progression[random.randint(0, len(progression) - 1)]
    true_answer_index = progression.index(true_answer)
    progression[true_answer_index] = ".."
    progression = " ".join(map(str, progression))
    num = f"{progression}"
    return num, str(true_answer)
