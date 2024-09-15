def evilChecker(a: int, b: int, c: int) -> str:
    """Древний алгоритм анализа треугольников на наличие зла"""

    sides = sorted([a, b, c])
    chanses = ["крайне мала", "велика", "100%"]
    if sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
        return chanses[0]
    elif sides[0] ** 2 + sides[1] ** 2 < sides[2] ** 2:
        return chanses[1]
    return chanses[2]


print(evilChecker(int(input()), int(input()), int(input())))
