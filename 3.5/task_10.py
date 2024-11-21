def main():
    INPUT_FILE = open(input(), mode="r", encoding="UTF-8")
    data = INPUT_FILE.readlines()
    tail_len = int(input())
    print(*data[-tail_len:], sep="")


if __name__ == "__main__":
    main()