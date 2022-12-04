from pathlib import Path
from string import ascii_letters


def parse(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()

    lines = input_string.strip().split('\n')

    return lines


letter_to_priority = {letter: ind + 1 for ind, letter in enumerate(ascii_letters)}


def solve_part_one(lines):
    total = 0

    for line in lines:
        half_ind = len(line) // 2

        first_set = set(line[:half_ind])
        second_set = set(line[half_ind:])
        total += letter_to_priority[
            list(first_set.intersection(second_set))[0]
        ]

    return total


def solve_part_two(lines):
    total = 0
    all_letters = set(ascii_letters)

    for i in range(0, len(lines), 3):
        common = all_letters
        for line in lines[i:i+3]:
            common = common.intersection(set(line))

        total += letter_to_priority[list(common)[0]]

    return total


if __name__ == "__main__":
    lines = parse(filename="input.txt")

    # part_one_answer = solve_part_one(lines)
    # print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(lines)
    print(f"Part Two Answer: {part_two_answer}")
