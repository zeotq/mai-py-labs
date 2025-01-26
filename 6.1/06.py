import numpy as np


def multiplication_matrix(size: int):
    cached_r = range(1, size + 1)
    return np.array([[i2 * i1 for i2 in cached_r] for i1 in cached_r])


def multiplication_matrix(size: int):
    ar = np.arange(1, size + 1)
    return np.outer(ar, ar)
    

def test_1():
    print(multiplication_matrix(3))

def test_2():
    print(multiplication_matrix(5))

if __name__ == "__main__":
    test_1()
    test_2()