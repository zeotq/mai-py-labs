import numpy as np
from typing import Literal


def rotate(arr, angle: Literal[90, 180, 270, 360]):
    if angle == 360:
        return arr
    if angle == 180:
        return arr[::-1, ::-1]
    if angle == 90:
        return arr[::-1, ::].transpose()
    if angle == 270:
        return arr[::, ::-1].transpose()

def test_1():
    print(rotate(np.arange(12).reshape(3, 4), 90))


def test_2():
    print(rotate(np.arange(12).reshape(3, 4), 270))


def test_3():
    print(rotate(np.arange(12).reshape(3, 4), 180))

if __name__ == "__main__":
    test_1()
    test_2()
    test_3()