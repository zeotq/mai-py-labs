def main():
    max_len = int(input())
    temp = []

    for _ in range(int(input())):
        string = input()
        temp.append(string)

    text = ''.join(temp)
    source_text = '\n'.join(temp)
    temp = ""

    if len(text) > max_len - 3:
        delta = 0
        for i in range(max_len - 3):
            if text[i] == source_text[i + delta]:
                temp += text[i]
            else:
                temp += "\n" + text[i]
                delta += 1
        text = temp + "..."

    print(text)
    

if __name__ == "__main__":
    main()
