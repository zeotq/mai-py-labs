def factorial(n: int) -> int:
    """Определение факториала числа"""

    answer, counter = 1, 1
    while counter <= n:
        answer *= counter
        counter += 1
    return answer


def poland_calc(data: str = '') -> int:
    
    intStack = []

    def isAction(a):
        return a in ["+", "-", "*", "/", "~", "!", "#", "@"]
    
    for i in data.split():
        if not isAction(i):
            intStack.append(int(i))
        else:
            match i:
                case "+" | "-" | "*" | "/":
                    if i == "+":
                        intStack[-2] = intStack[-1] + intStack[-2]
                    elif i == "-":
                        intStack[-2] = intStack[-2] - intStack[-1]
                    elif i == "*":
                        intStack[-2] = intStack[-2] * intStack[-1]
                    else:
                        intStack[-2] = intStack[-2] // intStack[-1]
                    intStack.pop(-1)
                case "~" | "!" | "#":
                    if i == "~":
                        intStack[-1] = intStack[-1] * (-1)
                    elif i == "!":
                        intStack[-1] = factorial(intStack[-1])
                    else:
                        intStack.append(intStack[-1])
                case "@":
                    intStack[-3], intStack[-2], intStack[-1] = intStack[-2], intStack[-1], intStack[-3]

    return intStack[0]


def main():
    print(poland_calc(input()))


if __name__ == "__main__":
    main()
