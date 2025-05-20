import numpy as np


def update_border(array, size, value):
    arr_copy = array.copy()
    flat = arr_copy.ravel()
    rows, cols = size

    if rows * cols != flat.size:
        raise ValueError()

    mat = flat.reshape(rows, cols)

    mat[0, :] += value
    mat[-1, :] += value

    if rows > 2:
        mat[1:-1, 0] += value
        mat[1:-1, -1] += value

    return mat.ravel().reshape(array.shape)


def test_1():
    array = np.arange(1, 16)
    print(array)
    new_array = update_border(array, (5, 3), 5)
    print(new_array)


def test_2():
    array = np.arange(1, 31)
    array.resize((3, 5, 2))
    print(array)
    new_array = update_border(array, (6, 5), 100)
    print(new_array)


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()