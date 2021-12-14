from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    coordinates, folds = set(), list()
    for line in input_string.strip().split('\n'):
        if not line:
            continue
        elif line.startswith('fold along'):
            axis, fold_number = line.split()[-1].split('=')
            folds.append((axis, int(fold_number)))
        else:
            coordinates.add(tuple(map(int, line.split(','))))
    return coordinates, folds


def update_coordinates(coordinates, folds):
    new_coordinates = set()
    removed_coordinates = set()

    for axis, fold_number in folds:
        for x, y in coordinates:
            if axis == 'y':
                if y == int(fold_number):
                    removed_coordinates.add((x, y))
                elif y > int(fold_number):
                    new_coordinates.add((x, fold_number - (y - fold_number)))
                    removed_coordinates.add((x, y))
            elif axis == 'x':
                if x == fold_number:
                    removed_coordinates.add((x, y))
                elif x > fold_number:
                    new_coordinates.add((fold_number - (x - fold_number), y))
                    removed_coordinates.add((x, y))

        coordinates = (coordinates | new_coordinates) - removed_coordinates

    return coordinates


def calculate_part1(coordinates, folds):
    coordinates = update_coordinates(coordinates, folds)
    return len(coordinates)


def calculate_part2(coordinates, folds):
    coordinates = update_coordinates(coordinates, folds)

    max_x = max(coordinates, key=lambda x: x[0])[0]
    max_y = max(coordinates, key=lambda x: x[1])[1]

    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            if (x, y) in coordinates:
                line.append('🟡')
            else:
                line.append('⚫')
        print("".join(line))


if __name__ == '__main__':
    coordinates, folds = parse(filename="input.txt")

    part1_answer = calculate_part1(coordinates, folds[:1])
    print(part1_answer)

    calculate_part2(coordinates, folds)

