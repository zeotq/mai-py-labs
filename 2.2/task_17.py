from math import sqrt


def quadratic(a: int, b: int, c: int) -> tuple:
    """Поиск корней для уравнения вида ax^2 + bx + c = 0"""

    if a == 0 and b == 0 and c == 0:
        return ("Infinite solutions",)
    if a == 0:
        return ((round(-c / b, 2),) if b != 0 else ("No solution",))

    d = b ** 2 - 4 * a * c
    
    if d < 0: 
        return ("No solution",)
    elif d == 0:
        return (round(-b / (2 * a), 2), )
    return (round((-b + sqrt(d)) / (2 * a), 2), 
            round((-b - sqrt(d)) / (2 * a), 2))


a, b, c = [float(input()) for i in range(3)]
print(*sorted(quadratic(a, b, c)))