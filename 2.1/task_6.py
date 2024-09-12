def main(name: str, price: int, mass: int, money: int) -> str: 
    '''Эта функция возвращает текст чека'''
    
    text = (f"Чек\n" +
            f"{name} - {mass}кг - {price}руб/кг\n" +
            f"Итого: {mass * price}руб\n" +
            f"Внесено: {money}руб\n" + 
            f"Сдача: {money - mass * price}руб")

    return text


n = input()
pr, ms, mn = [int(input()) for i in range(3)]
print(main(n, pr, ms, mn))