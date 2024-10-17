def poland_calc_mini(data: str = '') -> int:

    intStack = []

    def isAction(a):
        return a in ["+", "-", "*"]
    
    for i in data.split():
        if not isAction(i):
            intStack.append(int(i))
        else:
            match i:
                case "+":
                    intStack[-2] = intStack[-1] + intStack[-2]
                case "-":
                    intStack[-2] = intStack[-2] - intStack[-1]
                case _:
                    intStack[-2] = intStack[-2] * intStack[-1]
            intStack.pop(-1)
    return intStack[0]


def main():
    print(poland_calc_mini(input()))


if __name__ == "__main__":
    main()
