def main():
    with open("3.5/task_17.txt", encoding='UTF-8') as f:
        print(''.join([chr(ord(i) % 128) for i in f.read()]))


if __name__ == "__main__":
    main()
