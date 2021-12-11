from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    lines = input_string.strip().split()
    return [list(map(int, line)) for line in lines]


def get_neighbors(r, c, matrix):
    left = matrix[r][c - 1] if c > 0 else None
    right = matrix[r][c + 1] if c < len(matrix[0]) - 1 else None
    up = matrix[r - 1][c] if r > 0 else None
    bottom = matrix[r + 1][c] if r < len(matrix) - 1 else None
    top_left = matrix[r - 1][c - 1] if r > 0 and c > 0 else None
    top_right = matrix[r - 1][c + 1] if r > 0 and c < len(matrix[0]) - 1 else None
    bottom_left = matrix[r + 1][c - 1] if r < len(matrix[0]) - 1 and c > 0 else None
    bottom_right = matrix[r + 1][c + 1] if r < len(matrix[0]) - 1 and c < len(matrix[0]) - 1 else None

    return [
        (left, r, c - 1),
        (right, r, c + 1),
        (up, r - 1, c),
        (bottom, r + 1, c),
        (top_left, r - 1, c - 1),
        (top_right, r - 1, c + 1),
        (bottom_left, r + 1, c - 1),
        (bottom_right, r + 1, c + 1)
    ]


def flash(r, c, matrix):
    total = 1
    neighbors = get_neighbors(r, c, matrix)
    matrix[r][c] = 0

    for neighbor, r, c in neighbors:
        if neighbor and matrix[r][c] != 0:
            matrix[r][c] += 1
            if matrix[r][c] > 9:
                total += flash(r, c, matrix)

    return total


def calculate_part1(energy_levels):
    total_flashes = 0

    for i in range(100):
        step_total = 0

        # 1st step: increment all energy levels by 1
        for r in range(len(energy_levels)):
            for c in range(len(energy_levels[0])):
                energy_levels[r][c] += 1

        # flash
        for r in range(len(energy_levels)):
            for c in range(len(energy_levels[0])):
                if energy_levels[r][c] > 9:
                    step_total += flash(r, c, energy_levels)

        total_flashes += step_total

    return total_flashes


def calculate_part2(energy_levels):
    total_flashes = 0
    i = 1

    while True:
        step_total = 0

        # 1st step: increment all energy levels by 1
        for r in range(len(energy_levels)):
            for c in range(len(energy_levels[0])):
                energy_levels[r][c] += 1

        # flash
        for r in range(len(energy_levels)):
            for c in range(len(energy_levels[0])):
                if energy_levels[r][c] > 9:
                    step_total += flash(r, c, energy_levels)

        if step_total == 100:
            return i

        total_flashes += step_total
        i += 1


if __name__ == '__main__':
    levels = parse(filename="input.txt")
    part1_answer = calculate_part1(levels)

    levels = parse(filename="input.txt")
    part2_answer = calculate_part2(levels)

    print(part1_answer, part2_answer)
