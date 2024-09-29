def main():
    n = int(input())
    for i in range(n):
        if input()[0].lower() not in ['а', 'б', 'в']:
            [input() for j in range(n - i - 1)]
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
