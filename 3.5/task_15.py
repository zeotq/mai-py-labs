from sys import stdin
from json import load


def tests_parser(tests_list):
    res_points = 0

    for block in tests_list:
        points = block.get('points')
        tests = block.get('tests')
        res = [1 if input() == test.get('pattern', None) else 0 for test in tests]
        res_points += sum(res) * points // len(res) 
    return res_points


def main():
    tests_file_name = "scoring.json"
    tests_file_name = "3.5/task_15.json"

    with open(tests_file_name, mode="r+", encoding="UTF-8") as f:
        source_tests = load(f)
    
    ppfi = tests_parser(source_tests)
    print(ppfi)


if __name__ == "__main__":
    main()
