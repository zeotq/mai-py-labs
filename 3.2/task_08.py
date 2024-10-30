def main():
    peoples = {}
    for _ in range(int(input())):
        temp = input().split()
        if temp[0] in peoples:
            peoples[temp[0]] += temp[1::]
        else:
            peoples[temp[0]] = temp[1::]

    type_of_food = input()
    return list(filter(lambda a: type_of_food in peoples[a], peoples))


if __name__ == "__main__":
    final = main()
    print("\n".join(sorted(final)) if len(final) != 0 else "Таких нет")
