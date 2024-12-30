def stMath(x, y, s):
    return list(range(x, y + 1, s)) + list(range(y, x - 1, -1 * s))


def main():
    a, b, step = int(input()), int(input()), int(input())
    print(*stMath(a, b, step), sep=" - ")


if __name__ == '__main__':
    main()