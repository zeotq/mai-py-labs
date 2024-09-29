def main():
    max_len = int(input())
    for i in range(int(input())):
        text = input()
        if len(text) > max_len:
            print(text[0:max_len - 3] + "...")
        else:
            print(text)


if __name__ == "__main__":
    main()
