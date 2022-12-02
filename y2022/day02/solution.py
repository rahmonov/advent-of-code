from enum import Enum
from pathlib import Path


class Move(Enum):
    rock = 'A'
    paper = 'B'
    scissors = 'C'

    def get_score(self):
        PLAYER_MOVE_TO_SCORE = {
            Move.rock: 1,
            Move.paper: 2,
            Move.scissors: 3
        }
        return PLAYER_MOVE_TO_SCORE[self]


class Result(Enum):
    lose = 'X'
    draw = 'Y'
    win = 'Z'

    def get_score(self):
        RESULT_TO_SCORE = {
            self.lose: 0,
            self.draw: 3,
            self.win: 6
        }
        return RESULT_TO_SCORE[self]


def parse_lines(filename):
    inputs_file = Path(__file__).parent / filename
    with open(inputs_file) as f:
        input_string = f.read()

    return input_string.strip().split('\n')


def parse_lines_for_part_one(lines):
    LETTER_TO_MOVE = {
        'A': Move.rock,
        'B': Move.paper,
        'C': Move.scissors,
        'X': Move.rock,
        'Y': Move.paper,
        'Z': Move.scissors,
    }

    moves = []
    for line in lines:
        x, y = line.split()
        moves.append((LETTER_TO_MOVE[x], LETTER_TO_MOVE[y]))

    return moves


def parse_lines_for_part_two(lines):
    parsed_inputs = []
    for line in lines:
        move, result = line.split()
        parsed_inputs.append((Move(move), Result(result)))

    return parsed_inputs


def solve_part_one(lines):
    moves = parse_lines_for_part_one(lines)

    def get_score(player_move: Move, enemy_move: Move):
        score = 0

        if enemy_move == player_move:
            score = 3
        elif enemy_move == Move.rock:
            score = 6 if player_move == Move.paper else 0
        elif enemy_move == Move.paper:
            score = 6 if player_move == Move.scissors else 0
        elif enemy_move == Move.scissors:
            score = 6 if player_move == Move.rock else 0

        return score + player_move.get_score()

    total_score = 0

    for opponent_move, my_move in moves:
        total_score += get_score(player_move=my_move, enemy_move=opponent_move)

    return total_score


def solve_part_two(lines):
    parsed_inputs = parse_lines_for_part_two(lines)

    def get_score(enemy_move: Move, result: Result):
        score = 0

        if result == Result.draw:
            score = enemy_move.get_score()
        elif result == Result.lose:
            MOVE_TO_LOSER_MOVE = {
                Move.rock: Move.scissors,
                Move.paper: Move.rock,
                Move.scissors: Move.paper
            }
            score = MOVE_TO_LOSER_MOVE[enemy_move].get_score()
        elif result == Result.win:
            MOVE_TO_WINNER_MOVE = {
                Move.rock: Move.paper,
                Move.paper: Move.scissors,
                Move.scissors: Move.rock
            }
            score = MOVE_TO_WINNER_MOVE[enemy_move].get_score()

        return score + result.get_score()

    total_score = 0
    for enemy_move, result in parsed_inputs:
        total_score += get_score(enemy_move, result)

    return total_score


if __name__ == "__main__":
    lines = parse_lines(filename="input.txt")

    part_one_answer = solve_part_one(lines)
    print(f"Part One Answer: {part_one_answer}")

    part_two_answer = solve_part_two(lines)
    print(f"Part Two Answer: {part_two_answer}")
