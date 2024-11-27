old_sents = set()


def modern_print(sent: str) -> None:
    global old_sents
    if sent in old_sents:
        return
    print(sent)
    old_sents.add(sent)


def main():
    modern_print("Hello!")
    modern_print("Hello!")
    modern_print("How do you do?")
    modern_print("Hello!")


if __name__ == "__main__":
    main()