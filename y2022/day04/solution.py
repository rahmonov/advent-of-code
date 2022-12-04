from pathlib import Path
from typing import List


def parse(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()

    lines = input_string.strip().split('\n')
    pairs = []
    for line in lines:
        parts = line.split(',')
        part_one = list(map(int, parts[0].split('-')))
        part_two = list(map(int, parts[1].split('-')))
        pairs.append([part_one, part_two])

    return pairs


def solve_part_one(pairs: List[List]):
    count = 0
    for pair in pairs:
        pair.sort(key=lambda x: (x[0], -x[1]))

        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            count += 1

    return count


def solve_part_two(pairs):
    count = 0
    for pair in pairs:
        pair.sort(key=lambda x: (x[0], x[1]))

        if pair[1][0] <= pair[0][1]:
            count += 1

    return count


if __name__ == "__main__":
    pairs = parse(filename="test_input.txt")

    part_one_answer = solve_part_one(pairs)
    print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(pairs)
    print(f"Part Two Answer: {part_two_answer}")
