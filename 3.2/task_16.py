def find_neighbors(target: str = "зайка") -> set:
    neighbor_entitys = set()

    while (line := input()) != "": 
        line = line.split()
        len_line = len(line)
        for index, el in enumerate(line):
            if el == target:
                if index + 1 == len_line:
                    neighbor_entitys.add(line[index - 1])
                elif index == 0:
                    neighbor_entitys.add(line[index + 1])
                else:
                    neighbor_entitys.add(line[index - 1])
                    neighbor_entitys.add(line[index + 1])
    return neighbor_entitys
        

if __name__ == "__main__":
    final = find_neighbors()
    for i in final:
        print(i)
