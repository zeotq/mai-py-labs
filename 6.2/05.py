import pandas as pd


def get_long(data_frame: pd.Series, min_length: int = 5):
    filtered_frame = data_frame[data_frame >= min_length]
    return filtered_frame


def test_1():
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data)
    print(data)
    print(filtered)


def test_2():
    data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
    filtered = get_long(data, min_length=6)
    print(data)
    print(filtered)


if __name__ == "__main__":
    test_1()
    test_2()
