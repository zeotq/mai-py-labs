from itertools import permutations


def main():
    names = []
    for _ in range(int(input().strip())):
        names.extend(input().replace(",", "").split())
    names.sort()

    stands = list(permutations(names, r=3))
    for i in stands:
        print(*i, sep=" ", end="\n")


if __name__ == "__main__":
    main()