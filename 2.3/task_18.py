def isPrime(n: int) -> bool:
    """Определение простого числа
    
    Args:
        n (int): некоторое число
    
    Returns:
        bool: истина / ложь
    """

    if n in [-1, 0, 1]:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primeFinder(n: int) -> tuple:
    """Поиск простых чисел делителей для данного числа.

    Args:
        n (int): некоторое число

    Returns:
        primes (turple): простые числа делители исходного числа
    """
    
    primes = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0 and isPrime(i):
            primes.append(i)
        if isPrime(n // i):
            primes.append(n // i)
    return sorted(primes)


def primeFactorization(n: int, primes: list) -> list:
    """Разложение числа на простые множители.

    Args:
        n (int): некоторое число
        primes (turple): простые делители числа

    Returns:
        primes_fact (list): простые числа делители исходного числа
    """
    
    primes_fact = []
    while n != 1:
        prime_max_temp = max([i for i in primes if n % i == 0])
        primes_fact.append(prime_max_temp)
        n //= prime_max_temp
    return list(reversed(primes_fact))


def main():
    a = int(input())
    if isPrime(a):
        print(a)
    else:
        print(*primeFactorization(a, primes=primeFinder(a)), sep=" * ")


if __name__ == "__main__":
    main()