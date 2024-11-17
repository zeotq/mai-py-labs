from itertools import product


def numericRectangle(y: int | None = 2, x: int | None = 3) -> list:
    result = [[0] * x for _ in range(y)]
    for i, (row, col) in enumerate(product(range(y), range(x)), start=1):
        result[row][col] = i
    return result


def main():
    N = int(input().strip())
    M = int(input().strip())

    res = numericRectangle(N, M)
    max_width = len(str(N * M))

    for i in res:
        for j in i:
            print(f"{(max_width - len(str(j))) * ' '}{j}", end=' ')
        print()


if __name__ == "__main__":
    main()