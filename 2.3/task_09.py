def factorial(n: int) -> int:
    """Определение факториала числа"""

    answer, counter = 1, 1
    while counter <= n:
        answer *= counter
        counter += 1
    return answer


print(factorial(int(input())))