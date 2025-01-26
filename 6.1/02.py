from math import gcd
from sys import stdin


def lines_gcd() -> int:
    for line in stdin:
        print(gcd(*map(int, line.split())))


if __name__ == "__main__":
    lines_gcd()