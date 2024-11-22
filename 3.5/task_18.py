from os import path


def size_from_sys(file_path):
    return path.getsize(file_path)


def size_from_bits(file_path):
    bit_count = 0  # Счетчик битов

    with open(file_path, mode="rb") as f:
        byte = f.read(1)
        
        while byte:
            bit_count += 1
            byte = f.read(1)


def main():
    bit_count = size_from_sys(input())
    if bit_count >= 1024**3:
        bit_count = f'{int(bit_count / 1024**3) + 1}ГБ'
    elif bit_count >= 1024**2:
        bit_count = f'{int(bit_count / 1024**2) + 1}МБ'
    elif bit_count >= 1024:
        bit_count = f'{int(bit_count / 1024) + 1}КБ'
    else:
        bit_count = f'{int(bit_count)}Б'
    print(bit_count)


if __name__ == "__main__":
    main()