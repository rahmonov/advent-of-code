import functools
from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    lines = input_string.strip().split()
    return [list(map(int, line)) for line in lines]


def is_low_point(r, c, matrix):
    left = matrix[r][c - 1] if c > 0 else float("inf")
    right = matrix[r][c + 1] if c < len(matrix[0]) - 1 else float("inf")
    up = matrix[r - 1][c] if r > 0 else float("inf")
    bottom = matrix[r + 1][c] if r < len(matrix) - 1 else float("inf")
    return all(matrix[r][c] < neighbor for neighbor in (left, right, up, bottom))


def calculate_part1(matrix):
    sum_risk = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if is_low_point(r, c, matrix):
                sum_risk += matrix[r][c] + 1

    return sum_risk


def get_basin_size(r, c, matrix, came_from, seen):
    if (r, c) in seen:
        return 0

    current_total = 1
    seen.add((r, c))

    left = matrix[r][c - 1] if c > 0 else None
    if left and came_from != "left" and left != 9 and left > matrix[r][c]:
        current_total += get_basin_size(r, c - 1, matrix, came_from="right", seen=seen)

    right = matrix[r][c + 1] if c < len(matrix[0]) - 1 else None
    if right and came_from != "right" and right != 9 and right > matrix[r][c]:
        current_total += get_basin_size(r, c + 1, matrix, came_from="left", seen=seen)

    up = matrix[r - 1][c] if r > 0 else None
    if up and came_from != "up" and up != 9 and up > matrix[r][c]:
        current_total += get_basin_size(r - 1, c, matrix, came_from="bottom", seen=seen)

    bottom = matrix[r + 1][c] if r < len(matrix) - 1 else None
    if bottom and came_from != "bottom" and bottom != 9 and bottom > matrix[r][c]:
        current_total += get_basin_size(r + 1, c, matrix, came_from="up", seen=seen)

    return current_total


def calculate_part2(matrix):
    basins = []

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if is_low_point(r, c, matrix):
                seen = set()
                basins.append(
                    get_basin_size(r, c, matrix, came_from="low_point", seen=seen)
                )

    largest_three = sorted(basins)[-3:]

    return functools.reduce(lambda x, y: x * y, largest_three)


if __name__ == '__main__':
    matrix = parse(filename="input.txt")

    part1_answer = calculate_part1(matrix)
    part2_answer = calculate_part2(matrix)

    print(part1_answer, part2_answer)
