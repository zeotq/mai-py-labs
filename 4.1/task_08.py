def is_palindrome(word: any) -> bool:
    if isinstance(word, int):
        word = str(word)
    return word[::-1] == word


def main():
    result = is_palindrome(123)
    print(result)
    result = is_palindrome([1, 2, 1, 2, 1])
    print(result)
    result = is_palindrome(tuple([1, 2, 1, 2, 1]))
    print(result)


if __name__ == "__main__":
    main()
