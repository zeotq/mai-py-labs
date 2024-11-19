def main():
    numbers = [1, 2, 3, 4, 5]
    data = [i for i in numbers if i % 2 == 0] + [i for i in numbers if i % 2 == 1]
    print(data)


if __name__ == "__main__":
    main()