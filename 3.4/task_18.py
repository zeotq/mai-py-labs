from itertools import product


def main():
    source_function = input()
    print("a b c f")
    for a, b, c in reversed(list(product([1, 0], repeat=3))):
        print(a, b, c, end=" ")
        print("1" if eval(source_function) else "0")


if __name__ == "__main__":
    main()