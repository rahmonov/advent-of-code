from collections import defaultdict
from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    graph = defaultdict(list)
    for line in input_string.strip().split():
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)
    return graph


def get_path_count(path, graph, seen_already):
    if path[-1] == "end":
        return 1

    path_count = 0
    for next_start in graph[path[-1]]:
        if not (next_start.islower() and next_start in path):
            path_count += get_path_count(path + (next_start, ), graph, seen_already)
        elif not seen_already and next_start != "start":
            path_count += get_path_count(path + (next_start, ), graph, True)

    return path_count


def calculate_part1(graph):
    return get_path_count(('start', ), graph, True)


def calculate_part2(graph):
    return get_path_count(('start', ), graph, False)


if __name__ == '__main__':
    graph = parse(filename="test_input.txt")

    part1_answer = calculate_part1(graph)
    part2_answer = calculate_part2(graph)

    print(part1_answer, part2_answer)
