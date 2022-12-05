from pathlib import Path


def parse(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()

    lines = input_string.split('\n')
    total_stacks = _get_total_stacks(lines)
    stacks = [[] for _ in range(total_stacks)]
    moves = []

    for line in lines:
        if line.strip().startswith('1'):
            break

        for i in range(total_stacks):
            crate = _get_nth_crate(line, i)
            if crate != ' ':
                stacks[i].append(crate)

    for line in lines:
        if line.startswith('move'):
            moves.append(_parse_move(line))

    for i in range(total_stacks):
        stacks[i].reverse()

    return stacks, moves


def _parse_move(line):
    parts = line.split()
    return int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1


def _get_nth_crate(stacks, n):
    return stacks[n * 3 + n + 1]


def _get_total_stacks(lines):
    for line in lines:
        line = line.strip()
        if line.startswith('1'):
            return int(line[-1])


def solve_part_one(stacks, moves):
    for crate_count, from_col, to_col in moves:
        for _ in range(crate_count):
            stacks[to_col].append(stacks[from_col].pop())

    result = "".join([stack[-1] for stack in stacks])

    return result


def solve_part_two(stacks, moves):
    for crate_count, from_col, to_col in moves:
        to_add = []

        for _ in range(crate_count):
            to_add.append(stacks[from_col].pop())

        for _ in range(len(to_add)):
            stacks[to_col].append(to_add.pop())

    result = "".join([stack[-1] for stack in stacks])

    return result


if __name__ == "__main__":
    stacks, moves = parse(filename="input.txt")

    part_one_answer = solve_part_one(stacks, moves)
    print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(stacks, moves)
    print(f"Part Two Answer: {part_two_answer}")
