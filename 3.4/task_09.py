from itertools import product


def multTable(size):
    row = list(range(1, size + 1))
    elements = list(product(row, row))

    return list(map(lambda multEl: multEl[0] * multEl[1], elements))


def main():
    size_of_table = int(input())
    table = multTable(size_of_table)
    index_of_element = 0
    while index_of_element < size_of_table ** 2:
        print(table[index_of_element], end=' ')
        if (index_of_element + 1) % size_of_table == 0:
            print()
        index_of_element += 1


if __name__ == "__main__":
    main()
