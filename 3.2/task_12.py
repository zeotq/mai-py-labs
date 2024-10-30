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
    temp = inputPeoples(int(input()))
    sorted_dict = dict(sorted(temp.items()))

    isEmpty = True
    for i in sorted_dict:
        act = sorted_dict[i]
        if act > 1:
            isEmpty = False
            print(f'{i} - {act}')

    if isEmpty:
        print("Однофамильцев нет")


if __name__ == "__main__":
    main()
