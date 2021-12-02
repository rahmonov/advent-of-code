def get_position(moves):
    horizontal_pos = depth = 0

    for move in moves:
        move = move.split()

        if move[0] == 'forward':
            horizontal_pos += int(move[1])
        elif move[0] == 'up':
            depth -= int(move[1])
        else:
            depth += int(move[1])

    return horizontal_pos * depth
