from itertools import product


alphabet = ["А", "Б", "В"]


def formatPermutations(count: int, heading: set):
    result = list()
    result.append(list(heading))

    variants = product([i for i in range(1, count + 1)], repeat=len(heading))
    good_variants = list(filter(lambda a: sum(a) == count, list(variants)))
    result += good_variants

    return result


def main():
    data = formatPermutations(int(input()), alphabet)
    for i in data:
        print(*i)


if __name__ == "__main__":
    main()