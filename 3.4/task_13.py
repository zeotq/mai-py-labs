from itertools import permutations


def main():
    names = []
    for _ in range(int(input().strip())):
        names.append(input())
    names.sort()

    stands = list(permutations(names, r=len(names)))
    for i in stands:
        print(*i, sep=", ", end="\n")


if __name__ == "__main__":
    main()