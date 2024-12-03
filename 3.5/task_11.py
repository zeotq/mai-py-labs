import json


def main():
    # file_in = input()
    # file_out = input()
    file_in = "task_7_in.txt"
    file_out = "task_11_out.json"
    FILE_INPUT = open(file_in, encoding="UTF-8")
    FILE_OUTPUT = open(file_out, mode="w", encoding="UTF-8")

    nums = list()
    for line in FILE_INPUT.readlines():
        nums += list(map(int, line.split()))

    res = {"count": len(nums),
           "positive_count": len(list(filter(lambda n: abs(n) == n and n != 0, nums))),
           "min": min(nums),
           "max": max(nums),
           "sum": sum(nums), 
           "average": round(sum(nums) / len(nums), 2)}

    json.dump(res, FILE_OUTPUT, indent=4, ensure_ascii=False)
    FILE_INPUT.close()
    FILE_OUTPUT.close()


if __name__ == "__main__":
    main()