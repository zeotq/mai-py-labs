def cz_encoder(word: iter, shift: int) -> str:
    """Make bytes shift for latin charecters

    Args:
        word (iter): any word
        shift (int): shift value

    Returns:
        str: new_word
    """
    new_word = str()
    for i in word:
        if 65 <= i <= 90:
            new_char = chr(65 + (i + shift - 65) % 26)
        elif 97 <= i <= 122:
            new_char = chr(97 + (i + shift - 97) % 26)
        else:
            new_char = chr(i)
        new_word += new_char
    return new_word


def main():
    with open("3.5/task_19_in.txt", encoding='UTF-8') as f:
        data = [ord(i) for i in f.read()]

    shift = int(input())
    result = cz_encoder(data, shift)

    with open("3.5/task_19_out.txt", mode="w", encoding='UTF-8') as f:
        f.writelines(result)


if __name__ == "__main__":
    main()