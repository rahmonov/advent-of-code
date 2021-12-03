from collections import defaultdict


def get_power_consumption(bin_nums):
    counter = defaultdict(int)
    for bin_num in bin_nums:
        for idx, bit in enumerate(bin_num):
            counter[idx] += 1 if bit == '1' else -1

    gamma_rate = epsilon_rate = ''
    for i in range(len(bin_nums[0])):
        gamma_rate += '1' if counter[i] > 0 else '0'
        epsilon_rate += '0' if counter[i] > 0 else '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

