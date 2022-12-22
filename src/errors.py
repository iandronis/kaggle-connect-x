from kaggle_environments.errors import CanonicalError


class InvalidMoveException(CanonicalError):
    def __init__(self, error=""):
        super().__init__(error, "INVALID_MOVE")
