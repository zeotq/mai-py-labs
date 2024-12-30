from itertools import combinations


def count_pairs(*args, div: int = 10):
    result = 0
    for i in list(combinations(args, r=2)):
        if (i[0] + i[1]) % div == 0:
            print(i)
            result += 1
    return result


def main():
    numbers = [41, 56, 54, 6, 31, 81, 77, 83, 86, 15]
    result = count_pairs(*numbers, div=3)
    print(result)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = count_pairs(*numbers)
    print(result)


if __name__ == "__main__":
    main()