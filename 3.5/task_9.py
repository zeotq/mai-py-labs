def main():
    f_input, f_output = [input() for _ in range(2)]

    with open(f_input, mode="r", encoding="UTF-8") as fin, open(f_output, mode="w+", encoding="UTF-8") as fout:
        new = [line.rstrip().replace("\t", "").split() for line in fin.readlines() if line != "\n"]
        for line in new:
            fout.write(" ".join(line) + "\n")
    fin.close()


if __name__ == "__main__":
    main()
# task_9_in.txt task_9_out.txt