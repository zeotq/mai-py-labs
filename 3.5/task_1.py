from sys import stdin


def main():
    res = 0
    for line in stdin:
        res += sum(list(map(int, line.split())))
    print(res)


if __name__ == "__main__":
    main()