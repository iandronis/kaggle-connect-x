import random

from src import utils

BOARD_MARKS = [1, 2]


def agent_template(obs, config) -> int:
    """Return the agent's next move, i.e. the column's index."""


def agent_random(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return random.choice(valid_moves)


def agent_middle(obs, config):
    """
    Note. This might give some invalid moves.
    """
    return config.columns // 2


def agent_leftmost(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return valid_moves[0]


def agent_random_prefer_winning_move(obs, config):
    board = utils.convert_board_1d_to_2d(obs.board, config)
    agent_piece = obs.mark

    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    for move in valid_moves:
        if utils.check_winning_move(board, config, move, agent_piece):
            return move

    return random.choice(valid_moves)


def agent_random_prefer_winning_avoid_losing_move(obs, config):
    board = utils.convert_board_1d_to_2d(obs.board, config)
    agent_piece = obs.mark

    valid_moves = [col for col in range(config.columns) if board[0][col] == 0]
    losing_moves = []
    for move in valid_moves:
        if utils.check_winning_move(board, config, move, agent_piece):
            return move

        opponent_piece = [mark for mark in BOARD_MARKS if mark != agent_piece][
            0
        ]
        if utils.check_losing_move(
            board, config, move, agent_piece, opponent_piece
        ):
            losing_moves.append(move)

    valid_moves_remove_losing = [
        move for move in valid_moves if move not in losing_moves
    ]
    # there are cases where you lose with any move you take
    if valid_moves_remove_losing:
        valid_moves = valid_moves_remove_losing
    return random.choice(valid_moves)


def agent_one_step_lookahead(obs, config):
    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]

    valid_moves_scores = []
    board = utils.convert_board_1d_to_2d(obs.board, config)
    for move in valid_moves:
        tmp_board = board.copy()
        utils.play_piece(tmp_board, config, move, obs.mark)
        valid_moves_scores.append(
            utils.heuristic_function(tmp_board, config, obs.mark)
        )

    max_score = max(valid_moves_scores)
    max_score_index = valid_moves_scores.index(max_score)
    return valid_moves[max_score_index]
