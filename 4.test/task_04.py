def index(iterable: str):
    for element in sorted(list(set(filter(lambda i: i.isalpha(), iterable)))):
        yield (element, iterable.index(element))


def main():
    text = "Мама мыла раму"
    for letter, i in index(text):
        print(f"{letter}: {i}")


if __name__ == "__main__":
    main()