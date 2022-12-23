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


def _discs_in_row_numb(
    board: np.ndarray,
    config,
    piece: int,
    discs_in_row: int,
    fast_break: bool = False,
) -> int:
    discs_in_row_numb = 0

    # horizontal
    for row in range(config.rows):
        for col in range(config.columns - (discs_in_row - 1)):
            window = list(board[row, col : col + discs_in_row])
            if window.count(piece) == discs_in_row:
                if fast_break:
                    return 1
                discs_in_row_numb += 1
    # vertical
    for row in range(config.rows - (discs_in_row - 1)):
        for col in range(config.columns):
            window = list(board[row : row + discs_in_row, col])
            if window.count(piece) == discs_in_row:
                if fast_break:
                    return 1
                discs_in_row_numb += 1
    # positive diagonal
    for row in range(config.rows - (discs_in_row - 1)):
        for col in range(config.columns - (discs_in_row - 1)):
            window = list(
                board[
                    range(row, row + discs_in_row),
                    range(col, col + discs_in_row),
                ]
            )
            if window.count(piece) == discs_in_row:
                if fast_break:
                    return 1
                discs_in_row_numb += 1
    # negative diagonal
    for row in range(discs_in_row - 1, config.rows):
        for col in range(config.columns - (discs_in_row - 1)):
            window = list(
                board[
                    range(row, row - discs_in_row, -1),
                    range(col, col + discs_in_row),
                ]
            )
            if window.count(piece) == discs_in_row:
                if fast_break:
                    return 1
                discs_in_row_numb += 1
    return discs_in_row_numb


def _check_board(board: np.ndarray, config, piece: int) -> bool:
    return (
        _discs_in_row_numb(
            board, config, piece, discs_in_row=config.inarow, fast_break=True
        )
        > 0
    )


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
