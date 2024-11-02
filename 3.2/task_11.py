def inputPeoples(count: int = 0) -> dict:
    peoples = {}
    for _ in range(count):
        name = input()
        if name in peoples:
            peoples[name] += 1
        else:
            peoples[name] = 1

    return peoples


def main():
    count = 0
    temp = inputPeoples(int(input()))
    for i in temp:
        if temp[i] > 1:
            count += temp[i]
    print(count)


if __name__ == "__main__":
    main()
