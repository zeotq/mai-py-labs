def main():
    len_1 = int(input())
    len_2 = int(input())
    peoples_1 = set([input() for i in range(len_1 + len_2)])

    if (max(len_1, len_2) == len(peoples_1)):
        print('Таких нет')
    else:
        print()

if __name__ == "__main__":
    main()
