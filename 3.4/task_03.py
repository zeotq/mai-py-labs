from itertools import count


def main():
    start, finish, step = list(map(float, input().split()))
    for value in count(start, step):
        if value <= finish:
            print(round(value, 1))
        else:
            break


if __name__ == "__main__":
    main()
