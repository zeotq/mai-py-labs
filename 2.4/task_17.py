def isPalidrome(word: str) -> bool:
    return word[::-1] == word


def main():
    print(len(list(filter(
        isPalidrome, 
        [input() for i in range(int(input()))]))))


if __name__ == "__main__":
    main()
