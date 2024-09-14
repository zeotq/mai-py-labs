def main(name: str, price: int, mass: int, money: int) -> str: 
    '''Эта функция возвращает красивый текст чека'''

    text = (f"================Чек================\n" +
            f"Товар:{" " * (29 - len(name))}{name}\n" +
            f"Цена:{" " * (19 - len(str(mass)) - len(str(price)))}" + 
            f"{mass}кг * {price}руб/кг\n" +
            f"Итого:{" " * (26 - len(str(mass * price)))}" +
            f"{mass * price}руб\n" +
            f"Внесено:{" " * (24 - len(str(money)))}{money}руб\n" + 
            f"Сдача:{" " * (26 - len(str(money - mass * price)))}" + 
            f"{money - mass * price}руб\n" +
            f"===================================")

    return text


n = input()
pr, ms, mn = [int(input()) for i in range(3)]
print(main(n, pr, ms, mn))