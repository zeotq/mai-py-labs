def main():
    while (word := input()): 
        if word[-3::] == "@@@":
            continue
        elif word[0:2] == "##":
            print(word[2::])
        else:
            print(word)


if __name__ == "__main__":
    main()
