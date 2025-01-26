import numpy as np


def make_board(size: int):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


def test_1():
    print(make_board(4))

def test_2():
    print(make_board(6))

if __name__ == "__main__":
    test_1()
    test_2()