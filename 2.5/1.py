def stMath(x, y, z):
    return f'({x} ^ {y}) mod ({x} + {z}) = {(x ** y) % (x + z)}'


def main():
    a, b, c = int(input()), int(input()), int(input())
    print(stMath(a, b, c))


if __name__ == '__main__':
    main()