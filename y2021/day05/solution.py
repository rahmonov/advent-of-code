from collections import defaultdict
from pathlib import Path


def parse(input_str):
    input_arr = []
    for line in input_str.strip().split('\n'):
        first_end, second_end = line.strip().split('->')
        first_end = list(map(int, first_end.strip().split(',')))
        second_end = list(map(int, second_end.strip().split(',')))
        input_arr.append((first_end, second_end))
    return input_arr


def calculate_part1(coordinates):
    counter = defaultdict(int)

    for coordinate in coordinates:
        x1, x2 = coordinate[0][0], coordinate[1][0]
        y1, y2 = coordinate[0][1], coordinate[1][1]

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                counter[f"{x1},{i}"] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                counter[f"{i},{y1}"] += 1

    response = 0
    for key in counter:
        if counter[key] >= 2:
            response += 1

    return response


def calculate_part2(coordinates):
    counter = defaultdict(int)

    for coordinate in coordinates:
        x1, x2 = coordinate[0][0], coordinate[1][0]
        y1, y2 = coordinate[0][1], coordinate[1][1]

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                counter[f"{x1},{i}"] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                counter[f"{i},{y1}"] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            x_direction = 1 if x2 > x1 else - 1
            y_direction = 1 if y2 > y1 else -1

            for x, y in zip(range(x1, x2 + x_direction, x_direction), range(y1, y2 + y_direction, y_direction)):
                counter[f"{x},{y}"] += 1

    response = 0
    for key in counter:
        if counter[key] >= 2:
            response += 1

    return response


if __name__ == '__main__':
    INPUTS_FILE = Path(__file__).parent / "input.txt"
    with open(INPUTS_FILE) as f:
        input_string = f.read()

    coordinates = parse(input_string)

    part1_answer = calculate_part1(coordinates)
    part2_answer = calculate_part2(coordinates)

    print(part1_answer, part2_answer)
