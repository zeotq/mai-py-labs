def main():
    """Возмедение в степень degree элементов массива integers
    """

    integers = list(map(int, input().split()))
    degree = int(input())

    integers = list(map(lambda a: pow(a, degree), integers))
    print(*integers, sep=" ")   


if __name__ == "__main__":
    main()
