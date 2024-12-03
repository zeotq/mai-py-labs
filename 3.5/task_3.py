from sys import stdin


def main():
    for line in stdin:
        cleaned = line.split("#", 1)[0].rstrip()
        if cleaned != "":
            print(cleaned)


if __name__ == "__main__":
    main()