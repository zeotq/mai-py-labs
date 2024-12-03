def merge(n: tuple, m: tuple) -> tuple:
    len_n, len_m = len(n), len(m)
    i, j = 0, 0
    result = [0] * (len_n + len_m)
    while (i + j) < (len_n + len_m):
        x = float('inf') if i >= len_n else n[i]
        y = float('inf') if j >= len_m else m[j]
        if x > y:
            result[i + j] = y
            j += 1
        else:
            result[i + j] = x
            i += 1

    return tuple(result)


def merge_sort(num_list):
    if len(num_list) > 1:
        mid_point = len(num_list) // 2
        before_mid = merge_sort(num_list[mid_point:])
        after_mid = merge_sort(num_list[:mid_point])
        return list(merge(before_mid, after_mid))
    return num_list


def main():
    result = merge_sort([3, 2, 1, 1448, 53, 668])
    print(result)


if __name__ == "__main__":
    main()