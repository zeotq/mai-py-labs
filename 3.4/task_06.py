from itertools import product


def genCards(rule_out_name: str = ''):
    names = ["пик", "треф", "бубен", "червей"]
    rangs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    if rule_out_name:
        names.remove(rule_out_name)
    values = list(product(rangs, names, repeat=1))
    return values


def main():
    for card in genCards(rule_out_name=input()):
        print(card[0], card[1])


if __name__ == "__main__":
    main()
