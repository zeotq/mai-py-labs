def generator(count: int = 1) -> list:
    """Бесполезная функция

    Args:
        count (int, optional): Количество гонщиков. Defaults to 1.

    Returns:
        list: Сообщения для системы оповещения. 
    """

    messages = {
        "w_0": "До старта",
        "w_1": "секунд(ы)",
        "s_0": "Старт",
        "s_1": "!!!"
    }
    
    allerts = []
    starts = 1
    while starts <= count:
        allerts.append("".join([f"{messages['w_0']} {i} {messages['w_1']}\n" for i in range(starts + 2, 0, -1)]))
        allerts.append(f"{messages['s_0']} {starts}{messages['s_1']}\n")
        starts += 1

    return allerts


def main():
    n = int(input())
    print(*generator(n), sep="")


if __name__ == "__main__":
    main()
