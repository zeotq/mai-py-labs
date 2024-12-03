def cycle(alist):
    index = 0
    while True:
        yield alist[index]
        index = (index + 1) % len(alist)


def main():
    print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
    print(*(x for _, x in zip(range(15), cycle([1, 2, 3, 4]))))


if __name__ == "__main__":
    main()