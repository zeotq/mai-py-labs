def enter_results(*args):
    global pairs
    if 'pairs' not in globals():
        pairs = []
    i = 0
    while i < len(args):
        pairs.append((args[i], args[i + 1]))
        i += 2


def get_sum() -> tuple:
    global pairs
    i_sum, j_sum = 0, 0
    for i, j in pairs:
        i_sum += i
        j_sum += j
    return (i_sum, j_sum)


def get_average() -> tuple:
    global pairs
    i_sum, j_sum = get_sum()
    return (i_sum / len(pairs), j_sum / len(pairs))


def main():
    enter_results(1, 2, 3, 4, 5, 6)
    print(pairs)
    print(get_sum(), get_average())
    enter_results(1, 2)
    print(get_sum(), get_average())


if __name__ == "__main__":
    main()