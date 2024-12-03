from sys import stdin


def main():
    lines = stdin.readlines()
    target = lines[-1].replace("\n", "").lower().rstrip()
    for index in range(0, len(lines) - 1):
        element = lines[index].rstrip()
        if target in element.lower():
            print(element)


if __name__ == "__main__":
    main()
