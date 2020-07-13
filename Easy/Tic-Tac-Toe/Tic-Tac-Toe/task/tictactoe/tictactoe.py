# write your code here


class TicTacToe:
    VALUE_X = "X"
    VALUE_O = "O"
    COORDS = [1, 2, 3]
    IMPOSSIBLE_STATE = "Impossible"
    X_WINS_STATE = f"{VALUE_X} wins"
    O_WINS_STATE = f"{VALUE_O} wins"
    DRAW_STATE = "Draw"
    GAME_NOT_FINISHED_STATE = "Game not finished"

    def __init__(self, state=None):
        self._state = state or "         "
        self._cells = [
            list(self._state[i:i + 3]) for i in range(0, len(self._state), 3)
        ]
        self._value = self.VALUE_X

    def _count(self, value):
        return self._state.count(value)

    def _win(self, value):
        fill = [value, value, value]
        combinations = self._cells[:]
        combinations.extend([
            [self._cells[0][0], self._cells[1][1], self._cells[2][2]],
            [self._cells[0][2], self._cells[1][1], self._cells[2][0]],
        ])
        combinations.extend([
            [self._cells[0][i], self._cells[1][i], self._cells[2][i]]
            for i in range(len(self._cells))
        ])
        return fill in combinations

    @property
    def state(self):
        return self._state

    @property
    def completed(self):
        return (
            " " not in self._state or
            self.status != self.GAME_NOT_FINISHED_STATE
        )

    @property
    def status(self):
        x_wins = self._win(self.VALUE_X)
        x_count = self._count(self.VALUE_X)
        o_wins = self._win(self.VALUE_O)
        o_count = self._count(self.VALUE_O)

        if (x_wins and o_wins) or (abs(x_count - o_count) > 1):
            return self.IMPOSSIBLE_STATE
        elif x_wins:
            return self.X_WINS_STATE
        elif o_wins:
            return self.O_WINS_STATE
        elif " " not in self._state:
            return self.DRAW_STATE
        return self.GAME_NOT_FINISHED_STATE

    def _change_value(self):
        self._value = (
            self.VALUE_O if self._value == self.VALUE_X else self.VALUE_X
        )

    def _update_state(self):
        self._state = "".join(cell for row in self._cells for cell in row)

    def set(self, x, y):
        x, y = 3 - x, y - 1
        if self._cells[x][y] in [self.VALUE_X, self.VALUE_O]:
            return False
        self._cells[x][y] = self._value
        self._change_value()
        self._update_state()
        return True

    def __str__(self):
        return (
            f"---------\n"
            f"| {' '.join(self._state[:3])} |\n"
            f"| {' '.join(self._state[3:6])} |\n"
            f"| {' '.join(self._state[6:9])} |\n"
            f"---------"
        )


def parse_input_position(data):
    data = data.split()
    if not data or not data[0].isdigit() or not data[1].isdigit():
        return "You should enter numbers!", None, None
    y, x = int(data[0]), int(data[1])
    if x not in TicTacToe.COORDS or y not in TicTacToe.COORDS:
        return "Coordinates should be from 1 to 3!", None, None
    return None, x, y


tic_tac_toe = TicTacToe()
print(tic_tac_toe)

while not tic_tac_toe.completed:
    message, pos_x, pos_y = parse_input_position(input(
        "Enter the coordinates: > "
    ))
    if message is not None:
        print(message)
    else:
        if not tic_tac_toe.set(pos_x, pos_y):
            print("This cell is occupied! Choose another one!")
        else:
            print(tic_tac_toe)

print(tic_tac_toe.status)
