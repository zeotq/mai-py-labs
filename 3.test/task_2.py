def main():
    words_from_litter = dict()

    while (line := input()) != "":
        for word in line.split():
            key_litter = word[-1].upper()
            if key_litter in words_from_litter.keys():
                words_from_litter[key_litter].update(set([word.lower()]))
            else:
                words_from_litter.update({key_litter: set([word.lower()])})

    for i in words_from_litter:
        print(f'{i} - ', end="")
        print(*list(sorted(words_from_litter[i])), sep=", ")


if __name__ == "__main__":
    main()