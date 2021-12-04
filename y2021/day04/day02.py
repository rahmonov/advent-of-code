from pathlib import Path

INPUTS_FILE = Path(__file__).parent / "input.txt"

with open(INPUTS_FILE) as f:
    input_str = f.read()
    parts = input_str.strip().split('\n')
    nums = parts[0].split(',')
    boards = []

    row_arr = []
    for input_row in parts[1:]:
        if input_row == '' and row_arr:
            boards.append(row_arr)
            row_arr = []
        elif input_row != '':
            row_arr.append(input_row.split())

    boards.append(row_arr)


def get_score(nums, boards):
    winning_board, winner_num = get_winning_board(nums, boards)

    unmarked_total = 0
    for r in range(len(winning_board)):
        for c in range(len(winning_board[0])):
            if winning_board[r][c] is not None:
                unmarked_total += int(winning_board[r][c])

    return unmarked_total * int(winner_num)


def get_winning_board(nums, boards):
    counter = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] for _ in range(len(boards))]
    won_boards = set()

    for num in nums:
        for idx, board in enumerate(boards):
            for r in range(len(board)):
                for c in range(len(board[0])):
                    if board[r][c] == num:
                        counter[idx][0][r] += 1
                        counter[idx][1][c] += 1
                        current_num = board[r][c]
                        board[r][c] = None  # mark

                        if counter[idx][0][r] == 5 or counter[idx][1][c] == 5:
                            if len(boards) - len(won_boards) == 1 and idx not in won_boards:
                                return board, current_num
                            won_boards.add(idx)


print(get_score(nums, boards))
