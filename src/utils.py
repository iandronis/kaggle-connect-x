import numpy as np

from src.errors import InvalidMoveException


def render_game(env):
    rendered_game_html = env.render(mode="html")
    with open("rendered_game.html", "w") as file:
        file.write(rendered_game_html)


def convert_board_1d_to_2d(board: list[int], config) -> np.ndarray:
    return np.asarray(board).reshape(config.rows, config.columns)


def play_piece(board: np.ndarray, config, col: int, piece: int) -> np.ndarray:
    if col not in range(config.columns):
        raise InvalidMoveException("Invalid move detected")

    for row in range(config.rows - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = piece
            return board

    raise InvalidMoveException("Invalid move detected")


def _check_board(board: np.ndarray, config, piece: int) -> bool:
    # horizontal
    for row in range(config.rows):
        for col in range(config.columns - (config.inarow - 1)):
            window = list(board[row, col : col + config.inarow])
            if window.count(piece) == config.inarow:
                return True
    # vertical
    for row in range(config.rows - (config.inarow - 1)):
        for col in range(config.columns):
            window = list(board[row : row + config.inarow, col])
            if window.count(piece) == config.inarow:
                return True
    # positive diagonal
    for row in range(config.rows - (config.inarow - 1)):
        for col in range(config.columns - (config.inarow - 1)):
            window = list(
                board[
                    range(row, row + config.inarow),
                    range(col, col + config.inarow),
                ]
            )
            if window.count(piece) == config.inarow:
                return True
    # negative diagonal
    for row in range(config.inarow - 1, config.rows):
        for col in range(config.columns - (config.inarow - 1)):
            window = list(
                board[
                    range(row, row - config.inarow, -1),
                    range(col, col + config.inarow),
                ]
            )
            if window.count(piece) == config.inarow:
                return True
    return False


def check_winning_move(board: np.ndarray, config, col: int, piece: int) -> bool:
    next_board = board.copy()
    play_piece(next_board, config, col, piece)
    return _check_board(next_board, config, piece)


def check_losing_move(
    board: np.ndarray, config, col: int, piece: int, opponent_piece: int
) -> bool:
    next_board = board.copy()
    play_piece(next_board, config, col, piece)

    opponent_valid_moves = [
        col for col in range(config.columns) if 0 in next_board[:][col]
    ]
    for opponent_move in opponent_valid_moves:
        if check_winning_move(
            next_board, config, opponent_move, opponent_piece
        ):
            return True
    return False
