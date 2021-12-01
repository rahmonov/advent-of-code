def count_increases(depths):
    count = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            count += 1

    return count
