def main(name: str, wardrobe: int) -> str: 
    '''Эта функция возвращает карточку ученика'''
    
    x = wardrobe // 100
    y = (wardrobe - x * 100) // 10
    z = wardrobe - x * 100 - y * 10

    text = (f"Группа №{x}.\n" +
            f"{z}. {name}.\n" +
            f"Шкафчик: {wardrobe}.\n" +
            f"Кроватка: {y}.\n") 

    return text


n, ord = input(), int(input())
print(main(n, ord))