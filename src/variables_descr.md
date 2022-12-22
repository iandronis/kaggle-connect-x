## obs
obs contains two pieces of information:
- obs.board - the game board (a Python list with one item for each grid location)
- obs.mark - the piece assigned to the agent (either 1 or 2)

## config
config contains three pieces of information:
- config.columns - number of columns in the game board (7 for Connect Four)
- config.rows - number of rows in the game board (6 for Connect Four)
- config.inarow - number of pieces a player needs to get in a row in order to win (4 for Connect Four)

```python
def agent(observation, configuration):
    # Number of Columns on the Board.
    columns = configuration.columns
    # Number of Rows on the Board.
    rows = configuration.rows
    # Number of Checkers "in a row" needed to win.
    inarow = configuration.inarow
    # The current serialized Board (rows x columns).
    board = observation.board
    # Which player the agent is playing as (1 or 2).
    mark = observation.mark

    # Return which column to drop a checker (action).
    return 0
```
