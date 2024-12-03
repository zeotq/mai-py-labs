from sys import stdin


def main():
    deltas = list()
    for line in stdin:
        name, height_before, height_after = line.split()
        delta_height = int(height_after) - int(height_before)
        deltas.append(delta_height)
    print(round(sum(deltas) / len(deltas)))


if __name__ == "__main__":
    main()