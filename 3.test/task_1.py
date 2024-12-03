def main():
    for _ in range(int(input())):
        slice_start, max_len, text = input().split("&")
        result = ""
        for i in range(int(slice_start), len(text), 2):
            result += text[i]
            if len(result) >= int(max_len):
                break
        print(result)


if __name__ == "__main__":
    main()