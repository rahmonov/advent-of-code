from pathlib import Path
from typing import List


def parse(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()
    datastream = input_string.strip()
    return datastream


def solve_part_one(datastream):
    for i in range(len(datastream)):
        if i > 2 and len(set(datastream[i-3:i+1])) == 4:
            return i + 1


def solve_part_two(datastream):
    for i in range(len(datastream)):
        if i > 13 and len(set(datastream[i - 13:i + 1])) == 14:
            return i + 1


if __name__ == "__main__":
    datastream = parse(filename="input.txt")

    part_one_answer = solve_part_one(datastream)
    print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(datastream)
    print(f"Part Two Answer: {part_two_answer}")
