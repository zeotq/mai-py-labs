def stMath(x, i):
    calc = -10**100
    for j in range(len(x) - 1):
        if abs(x[j] - x[j + 1]) < i:
            calc = max(calc, x[j + 1])
    return calc


def main():
    n, m = int(input()), int(input())
    data = [int(input()) for i in range(n)]
    print(stMath(data, m))


if __name__ == '__main__':
    main()