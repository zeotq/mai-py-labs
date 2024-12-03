def main():
    print(*filter(lambda a: sum([int(i) for i in str(abs(a))]) % 2 == 0, (32, 64, 128, 256, 512)))


if __name__ == "__main__":
    main()