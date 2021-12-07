from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    return list(map(int, input_string.strip().split(',')))


def calculate_part1(positions):
    min_fuel_spent = float("inf")

    for pos1 in positions:
        fuel_spent = 0
        for pos2 in positions:
            fuel_spent += abs(pos1 - pos2)
        min_fuel_spent = min(min_fuel_spent, fuel_spent)

    return min_fuel_spent


def calculate_part2(positions):
    min_fuel_spent = float("inf")
    max_position = max(positions)

    for pos1 in range(max_position):
        fuel_spent = 0
        for pos2 in positions:
            diff = abs(pos1 - pos2)
            fuel_spent += (diff * (diff + 1)) // 2

        min_fuel_spent = min(fuel_spent, min_fuel_spent)

    return min_fuel_spent


if __name__ == '__main__':
    positions = parse(filename="input.txt")

    part1_answer = calculate_part1(positions)
    part2_answer = calculate_part2(positions)

    print(part1_answer, part2_answer)
