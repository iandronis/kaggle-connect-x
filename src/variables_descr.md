## obs
obs contains two pieces of information:
- obs.board - the game board (a Python list with one item for each grid location)
- obs.mark - the piece assigned to the agent (either 1 or 2)

## config
config contains three pieces of information:
- config.columns - number of columns in the game board (7 for Connect Four)
- config.rows - number of rows in the game board (6 for Connect Four)
- config.inarow - number of pieces a player needs to get in a row in order to win (4 for Connect Four)
