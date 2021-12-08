from pathlib import Path


def parse(filename):
    INPUTS_FILE = Path(__file__).parent / filename
    with open(INPUTS_FILE) as f:
        input_string = f.read()
    lines = input_string.strip().split('\n')
    signal_patterns = [line.split('|')[0].strip().split(' ') for line in lines]
    output_values = [line.split('|')[1].strip().split(' ') for line in lines]
    return signal_patterns, output_values


def calculate_part1(output_values):
    count = 0

    for ov in output_values:
        for encoded_digit in ov:
            if len(encoded_digit) in [2, 4, 3, 7]:
                count += 1

    return count


def calculate_part2(signal_patterns, output_vals_arr):
    total = 0
    for pattern, output_values in zip(signal_patterns, output_vals_arr):
        total += get_output_val_for_entry(pattern, output_values)
    return total


def get_output_val_for_entry(pattern, output_values):
    known_nums = dict()
    unknown_len_5 = set()
    unknown_len_6 = set()

    for chars in pattern:
        if len(chars) == 2:
            known_nums[1] = set(chars)
        elif len(chars) == 3:
            known_nums[7] = set(chars)
        elif len(chars) == 4:
            known_nums[4] = set(chars)
        elif len(chars) == 7:
            known_nums[8] = set(chars)
        elif len(chars) == 5:
            unknown_len_5.add(chars)
        elif len(chars) == 6:
            unknown_len_6.add(chars)

    known_parts = dict()

    # find 2
    deleted_len_5_str = ""
    for any_len_5_str in unknown_len_5:
        if len((known_nums[4] | known_nums[7]) - set(any_len_5_str)) == 2:
            known_nums[2] = set(any_len_5_str)
            deleted_len_5_str = any_len_5_str
    unknown_len_5.remove(deleted_len_5_str)

    # find bottom_right
    known_parts['bottom_right'] = next(iter(known_nums[1] - known_nums[2]))

    # find upper_right
    known_parts['upper_right'] = next(iter(known_nums[1] - set(known_parts['bottom_right'])))

    # find 3
    deleted_len_5_str = ""
    for any_len_5_str in unknown_len_5:
        if known_parts['upper_right'] in any_len_5_str:
            known_nums[3] = set(any_len_5_str)
            deleted_len_5_str = any_len_5_str
    unknown_len_5.remove(deleted_len_5_str)

    # find 5
    known_nums[5] = set(next(iter(unknown_len_5)))

    # find 6
    deleted_len_6_str = ""
    for any_len_6_str in unknown_len_6:
        if set(any_len_6_str) == known_nums[8] - set(known_parts['upper_right']):
            known_nums[6] = set(any_len_6_str)
            deleted_len_6_str = any_len_6_str
    unknown_len_6.remove(deleted_len_6_str)

    # find bottom_left
    known_parts['bottom_left'] = next(iter(known_nums[6] - known_nums[5]))

    # find 9
    known_nums[9] = known_nums[8] - set(known_parts['bottom_left'])

    # find 0
    for any_len_6_str in unknown_len_6:
        if set(any_len_6_str) not in (known_nums[9], known_nums[6]):
            known_nums[0] = set(any_len_6_str)

    total = ""
    for ov in output_values:
        for num, char_set in known_nums.items():
            if set(ov) == char_set:
                total = total + str(num)

    return int(total)


if __name__ == '__main__':
    patterns, output_vals = parse(filename="input.txt")

    part1_answer = calculate_part1(output_vals)
    part2_answer = calculate_part2(patterns, output_vals)

    print(part1_answer, part2_answer)
