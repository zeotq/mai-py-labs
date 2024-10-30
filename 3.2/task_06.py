def main():
    peoples = {}
    for _ in range(int(input()) + int(input())):
        name = input()
        if name in peoples:
            peoples[name] += 1
        else:
            peoples[name] = 1
    peoples = list(filter(lambda a: peoples[a] == 1, peoples))

    if len(peoples) == 0:
        return "Таких нет"
    return "\n".join(sorted(peoples))  # единственное отличие от задания 5


if __name__ == "__main__":
    print(main())
