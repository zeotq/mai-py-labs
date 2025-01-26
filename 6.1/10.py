import numpy as np


def stairs(vec):
    new_arr = np.zeros((vec.size, vec.size), dtype=vec.dtype)
    for i in range(vec.size):
        new_arr[i] = np.roll(vec, i)
    return new_arr


def test_1():
    print(stairs(np.arange(3)))


def test_2():
    print(stairs(np.arange(5)))


if __name__ == "__main__":
    test_1()
    test_2()
