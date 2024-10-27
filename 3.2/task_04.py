def main():
    len_1, len_2 = int(input()), int(input())
    peoples_1 = set([input() for i in range(len_1)])
    peoples_2 = set([input() for j in range(len_2)])
    people_12 = peoples_1.intersection(peoples_2)
    if (list(people_12)):
        print(len(people_12))
    else:
        print('Таких нет')


if __name__ == "__main__":
    main()
