import random

from src.utils import convert_board_1d_to_2d, play_piece


def agent_random(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)


def agent_middle(obs, config):
    return config.columns // 2


def agent_leftmost(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return valid_moves[0]


def agent_random_check_winning_move(obs, config):
    board = convert_board_1d_to_2d(obs.board, config)
    agent_piece = obs.mark
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for move in valid_moves:
        if play_piece(board, move, agent_piece, config):
            return move
    return random.choice(valid_moves)
