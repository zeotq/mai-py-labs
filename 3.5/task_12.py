def main():
    # names = [input() for _ in range(4)]
    names = [f'task_12_{i + 1}.txt' for i in range(4)]
    FILE_NUMBERS = open(names[0], mode="r", encoding="UTF-8")
    FILE_EVEN = open(names[1], mode="w+", encoding="UTF-8")
    FILE_ODD = open(names[2], mode="w+", encoding="UTF-8")
    FILE_EQ = open(names[3], mode="w+", encoding="UTF-8")

    for line in FILE_NUMBERS.readlines():
        nums = list(map(int, line.split()))
        count_of_even = [sum([1 if int(i) % 2 == 0 else -1 for i in str(j)]) for j in nums]
        for index, value in enumerate(count_of_even):
            if value > 0:
                FILE_EVEN.write(f'{nums[index]} ')
            elif value < 0:
                FILE_ODD.write(f'{nums[index]} ')
            else:
                FILE_EQ.write(f'{nums[index]} ')
        FILE_EVEN.write('\n')
        FILE_ODD.write('\n')
        FILE_EQ.write('\n')

    FILE_NUMBERS.close()
    FILE_EVEN.close()
    FILE_ODD.close()
    FILE_EQ.close()


if __name__ == "__main__":
    main()