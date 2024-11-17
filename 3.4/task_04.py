from itertools import accumulate


def main():
    for string in accumulate([word + ' ' for word in input().split()]):
        print(string)


if __name__ == "__main__":
    main()
