def marker(x: int, y: int):
    marker = f'{x // 10}${y // 10}' 
    return marker


def treasure_opti_route(treasures: list) -> dict:
    ways = dict()
    for mark in treasures:
        if mark in ways:
            ways[mark] += 1
        else:
            ways[mark] = 1
    return ways


if __name__ == "__main__":
    coords_input = [marker(*(map(int, input().split()))) for i in range(int(input()))]
    print(max(treasure_opti_route(coords_input).values()))