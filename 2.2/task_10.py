def main(n) -> str:
    """Плохое шифрование"""

    m = [int(n[-1]) + int(n[-2]), int(n[-2]) + int(n[-3])]
    return f'{max(m)}{min(m)}'


print(main(input()))