def isPrime(n: int) -> bool:
    """Определение простого числа
    
    Args:
        n (int): некоторое число
    
    Returns:
        bool: истина / ложь
    """

    if n in [-1, 0, 1]:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print("YES" if isPrime(int(input())) else "NO")