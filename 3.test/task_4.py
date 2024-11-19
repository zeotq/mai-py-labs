from itertools import product


def main():
    digits = int(input())
    result = set()
    gruops = list()
    for i in range(digits):
        line = set(input().replace(",", " ").split())
        line = "".join([str(i) for i in line])
        gruops.append(line)
    result = list(sorted(product(*gruops, repeat=1)))

    for i in result:
        print(*i, sep="")


if __name__ == "__main__":
    main()