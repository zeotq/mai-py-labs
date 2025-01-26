import numpy as np
from typing import TypeAlias, Literal


Directions: TypeAlias = Literal["H", "V"]


def snake(columns: int, rows: int, direction: Directions = "H"):
    ar = np.arange(1, rows * columns + 1, dtype="int16")
    if direction == "H":
        board = np.reshape(ar, (rows, columns))
        board[1::2] = board[1::2, ::-1]
    elif direction == "V":
        board = np.reshape(ar, (columns, rows))
        board[1::2] = board[1::2, ::-1]
        board = board.transpose()
    else:
        raise ValueError("Wrong direction value")
    return board


def test_1():
    print(snake(5, 3))


def test_2():
    print(snake(5, 3, direction='V'))

if __name__ == "__main__":
    test_1()
    test_2()