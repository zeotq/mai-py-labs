def main(data: str) -> str:
    '''Эта функция из числа вида abcd составляет число badc'''

    return data[1] + data[0] + data[3] + data[2]


n = input()
print(main(n))
