import heapq
from pathlib import Path


def parse(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()

    lines = input_string.strip().split('\n')

    return lines


def solve_part_one(calory_lines):
    calory_lines.append("")

    current_sum = 0
    max_sum = 0

    for cal_line in calory_lines:
        if cal_line == '':
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += int(cal_line)

    return max_sum


def solve_part_two(calory_lines):
    calory_lines.append("")

    heap = []
    current_sum = 0

    for cal_line in calory_lines:
        if cal_line == '':
            heapq.heappush(heap, -1 * current_sum)
            current_sum = 0
        else:
            current_sum += int(cal_line)

    return sum(map(lambda x: x * -1, heapq.nsmallest(3, heap)))


if __name__ == "__main__":
    calory_lines = parse(filename="input.txt")

    part_one_answer = solve_part_one(calory_lines)
    print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(calory_lines)
    print(f"Part Two Answer: {part_two_answer}")
