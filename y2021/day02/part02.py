def get_position(moves):
    horizontal_pos = depth = aim = 0

    for move in moves:
        move = move.split()

        if move[0] == 'down':
            aim += int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])
        else:
            horizontal_pos += int(move[1])
            depth += int(move[1]) * aim

    return horizontal_pos * depth
