def main():
    """Возмедение в степень degree n элементов массива integers
    """

    n = int(input())
    integers = [int(input()) for i in range(n)]
    degree = int(input())

    integers = list(map(lambda a: pow(a, degree), integers))
    print(*integers, sep="\n")   


if __name__ == "__main__":
    main()
