def hashCheck4Legit(current_block: int, prev_block: int = 0) -> bool:
    """Проверка некоторого блока на легетимность.

    Проверка осуществляется путём сравнения
    вычисленного и представленного в блоке hash'а.

    Структура блока: Bn =  Mn * 256 ** 2 + Rn * 256 + Hn:
        Bn - блок
        Mn - натуральное число с полезной информацией
        Rn - случайное число от 0 до 255
        Hn - хэш блока

    Args:
        current_block (int): actual block 
        prev_block (int, optional): previus block. Defaults to 0.

    Returns:
        bool: is block legit.
    """

    prev_block_hash = prev_block % 256
    current_block_data = current_block // (256 ** 2)
    current_block_rand = (current_block // 256) % 256

    given_current_block_hash = current_block % 256
    real_current_block_hash = 37 * (prev_block_hash + 
                                    current_block_rand + 
                                    current_block_data) % 256

    # Хэш блока не должен быть больше 100
    if real_current_block_hash >= 100:
        return False
    if real_current_block_hash != given_current_block_hash:
        return False
    return True


def main():
    n = int(input())
    hashes = [int(input()) for i in range(n)]
    last_block = 0

    for index, element in enumerate(hashes):
        if not hashCheck4Legit(element, last_block):
            print(index)
            break
        last_block = element
    else:
        print(-1)
            

if __name__ == "__main__":
    main()
