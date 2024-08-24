import random

QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_challange():
    num = random.randint(1, 50)
    is_prime_flag = num > 1 and all(num % i for i in range
                                    (2, int(num**0.5) + 1))
    true_answer = "yes" if is_prime_flag else "no"
    return num, true_answer
