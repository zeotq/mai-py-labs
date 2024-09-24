def isPolidrom(n: str) -> bool:
    """Проверка строки на полидромность
    
    Args:
        n (str): строка для проверки
    """

    if n == n[::-1]:
        return True
    return False


if __name__ == '__main__':
    print("YES" if isPolidrom(input()) else "NO")