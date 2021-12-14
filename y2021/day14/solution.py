from collections import Counter
from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()

    lines = input_string.strip().split('\n')
    template = lines[0]
    insertions = dict()

    for line in lines[2:]:
        pair, new_ch = line.split('->')
        insertions[pair.strip()] = new_ch.strip()

    return template, insertions


def calculate(template, insertions, steps):
    char_counter = Counter(template)
    pairs = Counter()
    for i in range(len(template) - 1):
        pairs[template[i:i + 2]] += 1

    for step in range(steps):
        step_counter = Counter()

        for pair, new_ch in insertions.items():
            if pair in pairs and pairs[pair] > 0:
                step_counter[f"{pair[0]}{new_ch}"] += pairs[pair]
                step_counter[f"{new_ch}{pair[1]}"] += pairs[pair]

                char_counter[new_ch] += pairs[pair]
                step_counter[pair] -= pairs[pair]

        pairs += step_counter

    most_frequent = max([v for k, v in char_counter.items()])
    least_frequent = min([v for k, v in char_counter.items()])

    return most_frequent - least_frequent


def calculate_part1(template, insertions):
    return calculate(template, insertions, 10)


def calculate_part2(template, insertions):
    return calculate(template, insertions, 40)


if __name__ == '__main__':
    template, insertions = parse(filename="input.txt")

    part1_answer = calculate_part1(template, insertions)
    part2_answer = calculate_part2(template, insertions)

    print(part1_answer, part2_answer)
