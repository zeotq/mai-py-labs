def make_linear(alist: list) -> list:
    new_list = []
    for elemnet in alist:
        if isinstance(elemnet, list):
            new_list += make_linear(elemnet)
        else:
            new_list.append(elemnet)
    return new_list


def main():
    result = make_linear([1, 2, [3]])
    print(result)
    result = make_linear([1, [2, [3, 4]], 5, 6])
    print(result)


if __name__ == "__main__":
    main()