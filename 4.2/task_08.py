def main():
    string = 'Яндекс использует Python во многих проектах'
    print(list(sorted(string.split(), key=lambda a: (len(a), a.lower()))))


if __name__ == "__main__":
    main()