import numpy as np
import math


def avg_geom(nums: list[float]) -> float:
    nums_arr = np.array(nums)
    return math.pow(nums_arr.prod(), 1 / nums_arr.size)


if __name__ == "__main__":
    print(avg_geom(list(map(float, input().split()))))


def test_1():
    assert avg_geom([1, 2, 3, 4, 5,]) == 2.605171084697352

def test_2():
    assert avg_geom([1.1, 1.2, 1.3, 1.4, 1.5]) == 1.292252305460076