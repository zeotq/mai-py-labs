def merge(n: tuple, m: tuple) -> tuple:
    len_n, len_m = len(n), len(m)
    i, j = 0, 0
    result = [0] * (len_n + len_m)
    while (i + j) < (len_n + len_m):
        x = float('inf') if i >= len_n else n[i]
        y = float('inf') if j >= len_m else m[j]
        if x > y:
            result[i + j] = y
            j += 1
        else:
            result[i + j] = x
            i += 1

    return tuple(result)


def main():
    result = merge((1, 2), (3, 4, 5))
    print(result)
    result = merge((7, 12), (1, 9, 50))
    print(result)


if __name__ == "__main__":
    main()
