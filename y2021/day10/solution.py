from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    return input_string.strip().split()


CLOSING_TO_OPENING = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
OPENING_TO_CLOSING = {v: k for k, v in CLOSING_TO_OPENING.items()}


def calculate_part1(lines):
    POINT_TABLE = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    total_points = 0

    for line in lines:
        line_stack = []
        for ch in line:
            if ch in OPENING_TO_CLOSING:
                line_stack.append(ch)
            else:
                if not line_stack or line_stack[-1] != CLOSING_TO_OPENING[ch]:
                    total_points += POINT_TABLE[ch]
                    break
                else:
                    line_stack.pop()

    return total_points


def calculate_part2(lines):
    POINT_TABLE = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    total_points = []

    for line in lines:
        line_stack = []
        broken = False
        for ch in line:
            if ch in ('(', '[', '{', '<'):
                line_stack.append(ch)
            else:
                if line_stack and line_stack[-1] == CLOSING_TO_OPENING[ch]:
                    line_stack.pop()
                else:
                    broken = True

        if not line_stack or broken:
            continue

        line_points = 0
        # it means line is incomplete
        while line_stack:
            line_points = line_points * 5 + POINT_TABLE[OPENING_TO_CLOSING[line_stack.pop()]]

        total_points.append(line_points)

    total_points.sort()

    return total_points[len(total_points) // 2]


if __name__ == '__main__':
    lines = parse(filename="test_input.txt")

    part1_answer = calculate_part1(lines)
    part2_answer = calculate_part2(lines)

    print(part1_answer, part2_answer)
