#!/usr/bin/env python3
from brain_games.games import brain_even
from brain_games.game_engine import run_game_engine


def main():
    run_game_engine(brain_even)


if __name__ == "__main__":
    main()
