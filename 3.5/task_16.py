from sys import stdin


def main():
    #tests_files= ["3.5/task_16_1.txt", "3.5/task_16_2.txt"]
    #target = "a b".lower()
    target, *tests_files = [i.strip() for i in stdin]

    flag = False
    for i in tests_files:
        with open(i, mode="r", encoding="UTF-8") as f:
            text = " ".join(f.read().replace("&nbsp;", " ").lower().split())
            if target.lower() in text:
                flag = True
                print(i)
    if flag is False:
        print("404. Not Found")


if __name__ == "__main__":
    main()
