"""
https://adventofcode.com/2023/day/3

--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise.
"Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one.
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine.
There are lots of numbers and symbols you don't really understand, but
apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
    114 (top right) and 58 (middle right).
    Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger.
What is the sum of all of the part numbers in the engine schematic?

"""

import math
from profile import run
import re

INPUTS_PATH = "/Users/saisundarraghavan/github/AoC/2023/inputs/"
USE_EXAMPLE = False


def load_from_file(file_name="input3.txt"):
    if USE_EXAMPLE:
        return [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
    with open(INPUTS_PATH + file_name) as f:
        return f.read().splitlines()


matrix = load_from_file()


def return_gear_ratios(index, asterisk_matches, numbers_maps):
    running_sum = 0
    for asterisk_index in asterisk_matches:
        adjacent = []
        consider_nums = (
            numbers_maps[index - 1] + numbers_maps[index] + numbers_maps[index + 1]
        )
        for num, num_start, num_end in consider_nums:
            if not ((num_end < asterisk_index) or (num_start > asterisk_index + 1)):
                adjacent.append(int(num))
        running_sum += math.prod(adjacent) if len(adjacent) == 2 else 0

    return running_sum


def get_final_answer():
    result = 0
    numbers_maps = {}
    for index in range(len(matrix)):
        row = matrix[index]
        regex = re.compile(r"\d+")
        numbers_maps[index] = [
            (m.group(), m.start(), m.end()) for m in regex.finditer(row)
        ]

    for index in range(len(matrix)):
        row = matrix[index]
        matches = [m.start() for m in re.finditer(re.escape("*"), row)]
        result += return_gear_ratios(index, matches, numbers_maps)
    return result


if __name__ == "__main__":
    print(get_final_answer())
