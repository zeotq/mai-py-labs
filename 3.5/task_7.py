def main():
    # file_name = input()
    file_name = "task_7_in.txt"
    FILE_INPUT = open(file_name, encoding="UTF-8")

    nums = list()
    for line in FILE_INPUT.readlines():
        nums += list(map(int, line.split()))

    print(len(nums),
          len(list(filter(lambda n: abs(n) == n and n != 0, nums))),
          min(nums),
          max(nums),
          sum(nums),
          round(sum(nums) / len(nums), 2),
          sep="\n")
    FILE_INPUT.close()


if __name__ == "__main__":
    main()