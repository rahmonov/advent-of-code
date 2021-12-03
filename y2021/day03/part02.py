from collections import defaultdict


def get_life_support_rating(bin_nums):
    return get_rating(bin_nums, 0, 'oxygen_generator') * get_rating(bin_nums, 0, 'co2_scrubber')


def get_rating(bin_nums, i, rating_type):
    if len(bin_nums) == 1:
        return int(bin_nums[0], 2)

    counter = defaultdict(int)
    for bin_num in bin_nums:
        for idx, bit in enumerate(bin_num):
            counter[idx] += 1 if bit == '1' else -1

    eligible = []
    most_common_bit = get_most_common_bit(counter[i])

    for bin_num in bin_nums:
        if is_eligible(most_common_bit, bin_num[i], rating_type):
            eligible.append(bin_num)

    return get_rating(eligible, i + 1, rating_type)


def get_most_common_bit(freq):
    if freq == 0:
        return None

    return '1' if freq > 0 else '0'


def is_eligible(most_common_bit, current_bit, rating_type):
    if rating_type == 'oxygen_generator':
        return most_common_bit == current_bit if most_common_bit else current_bit == '1'
    else:
        return most_common_bit != current_bit if most_common_bit else current_bit == '0'
