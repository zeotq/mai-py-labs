from itertools import combinations


def genGameNet(players: list):
    values = list(combinations(players, 2))
    return values


def main():
    n = int(input())
    players = [input() for i in range(n)]
    table = genGameNet(players)

    for name_1, name_2 in table:
        print(f'{name_1} - {name_2}')


if __name__ == "__main__":
    main()
