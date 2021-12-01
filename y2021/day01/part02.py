def count_grouped_increases(depths):
    count = 0

    for i in range(1, len(depths) - 2):
        if sum(depths[i:i+3]) > sum(depths[i-1:i+2]):
            count += 1

    return count
