from collections import Counter
from pathlib import Path


def parse(input_str):
    return list(map(int, input_str.strip().split(',')))


def calculate_part1(days_arr, days=80):
    days_left = Counter(days_arr)

    for _ in range(days):
        new_days_left = {i: 0 for i in range(9)}

        for i in range(9):
            if i == 0:
                new_days_left[6] = days_left[0]
                new_days_left[8] = days_left[0]
            else:
                new_days_left[i - 1] += days_left[i]

        days_left = new_days_left

    return sum(days_left.values())


def calculate_part2(days_arr):
    return calculate_part1(days_arr, days=256)


if __name__ == '__main__':
    INPUTS_FILE = Path(__file__).parent / "input.txt"
    with open(INPUTS_FILE) as f:
        input_string = f.read()

    days_arr = parse(input_string)

    part1_answer = calculate_part1(days_arr)
    part2_answer = calculate_part2(days_arr)

    print(part1_answer, part2_answer)
