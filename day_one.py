"""
https://adventofcode.com/2023/day/1
"""

import re

INPUTS_PATH = "/Users/saisundarraghavan/github/AoC/2023/inputs/"
mock_file = False


def load_from_file(file_name="input1.txt"):
    if mock_file:
        return """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen""".splitlines()
    with open(INPUTS_PATH + file_name) as f:
        content = f.read().splitlines()

    return content


def reduce_each_line(line):
    numbers_in_words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    pattern = r"(" + "|".join(numbers_in_words.keys()) + r"|\d)"
    regex = re.compile(pattern)
    word_maps = {
        m.start(): (
            int(m.group()) if len(m.group()) == 1 else numbers_in_words[m.group()]
        )
        for m in regex.finditer(line)
    }
    return (word_maps[min(word_maps.keys())] * 10) + word_maps[max(word_maps.keys())]


def get_final_answer():
    result = [reduce_each_line(line) for line in load_from_file()]
    print(len(result))
    return sum(result)


if __name__ == "__main__":
    assert get_final_answer() == 53894, f"{get_final_answer()} != 53894"
