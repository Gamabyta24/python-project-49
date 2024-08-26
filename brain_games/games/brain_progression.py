import random

QUEST = "What number is missing in the progression?"


def game_challange():
    """Return the correct answer and question"""
    progression = is_progression()
    answer = progression[random.randint(0, len(progression) - 1)]
    answer_index = progression.index(answer)
    progression[answer_index] = ".."
    progression = " ".join(map(str, progression))
    question = f"{progression}"
    return question, str(answer)


def is_progression():
    """Return progression"""
    progression = []
    num_start = random.randint(1, 15)
    num_step = random.randint(1, 15)
    for _ in range(10):
        progression.append(num_start)
        num_start = num_start + num_step
    return progression
