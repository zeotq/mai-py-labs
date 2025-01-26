from math import comb


def seats_permutation(peoples: int, seats: int) -> tuple[int]:
    full = comb(peoples, seats)
    return (full - comb(peoples - 1, seats), full)


if __name__ == "__main__":
    print(*seats_permutation(*map(int, input().split())))