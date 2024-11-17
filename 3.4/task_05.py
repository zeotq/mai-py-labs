from itertools import chain


def main():
    data = sorted(list(chain.from_iterable([input().split(", ") for j in range(3)])))
    [print(f"{i}. {name}") for i, name in enumerate(data, 1)]


if __name__ == "__main__":
    main()
