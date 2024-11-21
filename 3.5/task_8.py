def read_files_to_sets(*args: str) -> list[set]:
    words_all_files = list()
    for file_name in args:
        FILE = open(file_name, encoding="UTF-8")
        words_from_file = set()
        words_from_file.update(*[i.split() for i in FILE.readlines()])
        words_all_files.append(words_from_file)
        FILE.close()
    return words_all_files


def main():
    n1, n2, nr = [input() for _ in range(3)]
    with open(nr, mode="a+", encoding="UTF-8") as f:
        w1, w2 = read_files_to_sets(n1, n2)
        res = list(sorted(w1 ^ w2))
        for i in res:
            f.write(f'{i}\n')


if __name__ == "__main__":
    main()
# task_8_in_1.txt
# task_8_in_2.txt
# task_8_out.txt