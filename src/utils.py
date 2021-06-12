import numpy as np
from kaggle_environments import InvalidArgument


def render_game(env):
    """
    Render into a relative html file and save it to play later.
    """
    my_html_file = env.render(mode="html")
    with open("my_html_file.html", "w") as file:
        file.write(my_html_file)


def convert_board_1d_to_2d(board: list[int], config) -> np.ndarray:
    return np.asarray(board).reshape(config.rows, config.columns)


def play_piece(board: np.ndarray, col: int, piece: int, config):
    invalid_move = True

    next_board = board.copy()
    for row in range(config.rows - 1, -1, -1):
        if next_board[row][col] == 0:
            invalid_move = False

    if invalid_move:
        raise InvalidArgument("Invalid move detected.")

    next_board[row][col] = piece
    return next_board


def check_winning_move(obs, config, col, piece):
    board = convert_board_1d_to_2d(board=obs.board, config=config)
    next_board = play_piece(board, col, piece, config)
    # horizontal
    for row in range(config.rows):
        for col in range(config.columns - (config.inarow - 1)):
            window = list(next_board[row, col : col + config.inarow])
            if window.count(piece) == config.inarow:
                return True
    # vertical
    for row in range(config.rows - (config.inarow - 1)):
        for col in range(config.columns):
            window = list(next_board[row : row + config.inarow, col])
            if window.count(piece) == config.inarow:
                return True
    # positive diagonal
    for row in range(config.rows - (config.inarow - 1)):
        for col in range(config.columns - (config.inarow - 1)):
            window = list(
                next_board[
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
                next_board[
                    range(row, row - config.inarow, -1),
                    range(col, col + config.inarow),
                ]
            )
            if window.count(piece) == config.inarow:
                return True
    return False
