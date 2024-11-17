def main():
    print(*[f'{i[0]} - {i[1]}' for i in list(zip(input().split(", "), input().split(", ")))], sep="\n")


if __name__ == "__main__":
    main()