def main():
    data = []
    for _ in range(int(input().strip())):
        data += input().replace(",", "").split()
    data.sort()

    for i, n in enumerate(data, start=1):
        print(f"{i}. {n}")
    

if __name__ == "__main__":
    main()