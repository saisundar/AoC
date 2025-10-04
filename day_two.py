"""
https://adventofcode.com/2023/day/2
"""

import math

INPUTS_PATH = "/Users/saisundarraghavan/github/AoC/2023/inputs/"
start_colors = {
    "red": 12,
    "blue": 14,
    "green": 13,
}
USE_EXAMPLE = False


def load_from_file(file_name="input2.txt"):
    if USE_EXAMPLE:
        return [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
    with open(INPUTS_PATH + file_name) as f:
        return f.read().splitlines()


def get_move_power(moves_list):
    round_colors = {}
    for move in moves_list:
        for colors in move.split(","):
            color = colors.split()[1]
            round_colors[color] = max(
                int(colors.split()[0]), round_colors.get(color, 0)
            )
    return math.prod(round_colors.values())


def get_final_answer():
    result = 0

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    #
    for game in load_from_file():
        [game_id_string, game_moves] = game.split(":")
        moves = game_moves.split(";")
        result += get_move_power(moves)
    return result


if __name__ == "__main__":
    print(get_final_answer())
