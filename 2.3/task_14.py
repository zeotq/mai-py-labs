def isSimple(n: int) -> bool:
    """Определение простого числа"""

    if n in [-1, 0, 1]:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print("YES" if isSimple(int(input())) else "NO")