from itertools import islice


def menu_table():
    '''
    Создание расписания подачи типов в соответсвии с количеством необходимых дней
    '''
    types_count = int(input())
    types = [input() for i in range(types_count)]
    days = int(input())
    result = []
    while days > types_count:
        result += (list(islice(types, 0, days)))
        days -= types_count
    else:
        result += (list(islice(types, 0, days)))
    
    return result


def main():
    print(*menu_table(), sep="\n")


if __name__ == "__main__":
    main()
