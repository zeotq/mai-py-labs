from itertools import product, combinations, chain


suits = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
card_values = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]


def main():
    name = input()
    value = input()

    good_card_values = list(card_values)
    good_card_values.remove(value)

    cards = product(good_card_values, suits.values())
    three_cards = sorted(combinations(cards, r=3))
    result = [row for row in three_cards if suits[name] in chain.from_iterable(row)]
    #result.sort()

    actual_position = tuple(tuple(i.split()) for i in input().split(", "))
    flag = False
    for i in result:
        if flag:
            print(', '.join(f'{rank} {suit}' for rank, suit in i))
            break
        elif actual_position == i:
            flag = True


if __name__ == "__main__":
    main()