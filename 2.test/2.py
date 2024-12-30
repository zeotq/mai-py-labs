def stMath(x, y, s):
    flagSpace = True if " " in s else False
    flagChet = True if len(s) % 2 == 0 else False

    if flagChet and flagSpace:
        return x + y
    elif flagChet and not flagSpace:
        return x - y
    elif not flagChet and flagSpace:
        return x * y
    return x // y


def main():
    a, s, b = int(input()), input(), int(input())
    print(stMath(a, b, s))


if __name__ == '__main__':
    main()