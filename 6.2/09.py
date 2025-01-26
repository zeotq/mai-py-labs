import pandas as pd


def filter_data_from_csv(lt_coords: tuple, rd_coords: tuple) -> pd.DataFrame:
    data_set = pd.read_csv("data.csv")
    return data_set[
        (lt_coords[0] <= data_set['x']) & (data_set['x'] <= rd_coords[0]) &
        (lt_coords[1] >= data_set['y']) & (data_set['y'] >= rd_coords[1])
    ]


def main():
    lt_coords = tuple(map(int, input().split()))
    rd_coords = tuple(map(int, input().split()))
    print(filter_data_from_csv(lt_coords, rd_coords))


if __name__ == "__main__":
    main()


def test_1():
    lt_coords = (0, 10)
    rd_coords = (10, 0)
    data = {
        'x': [9, 10, 10, 0, 3, 9, 7, 0, 0, 10, 8, 1, 4, 6, 10, 3, 1],
        'y': [0, 4, 5, 0, 1, 10, 0, 9, 3, 0, 4, 8, 3, 3, 10, 5, 2]
    }
    df = pd.DataFrame(data)
    df.index = [6262, 59060, 69882, 72739, 120951, 137931, 183595, 194157, 219910, 220920, 242318, 283651, 292990, 294474, 352959, 393223, 423449]
    assert df.equals(filter_data_from_csv(lt_coords, rd_coords))