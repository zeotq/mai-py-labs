def isPalidrome(word: str) -> bool:
    word = word.lower().replace(" ", "")
    return word[::-1] == word


def main():
    print("YES" if isPalidrome(input()) else "NO")


if __name__ == "__main__":
    main()
