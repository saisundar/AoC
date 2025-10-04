"""
https://adventofcode.com/2023/day/1
"""


def load_from_file(file_name):
    with open("input.txt", "r") as f:
        content = f.read().splitlines()

    return content


def reduce_each_line(line):
    if line == "":
        return 0

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

    word_maps = {}
    result = 0
    for word in numbers_in_words.keys():
        try:
            if line.find(word) != -1:
                word_maps[line.find(word)] = numbers_in_words[word]
            if line.rfind(word) != -1:
                word_maps[line.rfind(word)] = numbers_in_words[word]
        except ValueError as e:
            pass

    for index in range(len(line)):
        c = line[index]
        if c.isdigit():
            word_maps[index] = int(c)
    result += (word_maps[min(word_maps.keys())] * 10) + word_maps[max(word_maps.keys())]
    return result


def get_final_answer():
    file_name = ""

    list_of_lines = load_from_file(file_name)
    result = 0

    for line in list_of_lines:
        result += reduce_each_line(line)

    return result


if __name__ == "__main__":
    print(get_final_answer())
