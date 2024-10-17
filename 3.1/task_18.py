def rle(word: str, rle_data: list = [], prev: str = None) -> list:
    """RLE

    Args:
        word (str): any word
        rle_data (list, optional): rle to amend. Defaults to [].
        prev (str, optional): previous last symbol. Defaults to None.

    Returns:
        list: _description_
    """
    for element in word:
        if prev and element == prev:
            rle_data[-1][-1] += 1
        else:
            rle_data.append([element, 1])
        prev = element

    return rle_data


def main():
    rle_a = rle(input())
    for i in rle_a:
        print(*i)


if __name__ == "__main__":
    main()
