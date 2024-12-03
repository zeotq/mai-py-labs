from sys import stdin


def isPalidrome(word: str) -> bool:
    return word[::-1].lower() == word.lower()


def main():
    pwords = set()
    lines = stdin.readlines()
    for line in lines:
        for word in line.split():
            if isPalidrome(word):
                pwords.add(word)
    print(*sorted(pwords), sep="\n")

        
if __name__ == "__main__":
    main()
