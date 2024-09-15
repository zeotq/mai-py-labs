def sysDanger(x, y):
    """Система предупреждения опасности"""
    
    status = ""
    if x ** 2 + y ** 2 > 100:
        status = "water"
    elif (y >= 0.25 * x ** 2 + 0.5 * x - 8.75 and y < 0 or 
          x ** 2 + y ** 2 <= 25 and x >= 0 and y >= 0 or
          y <= 5 and y >= 0 and x <= 0 and x >= -4 or
          x >= 0.6 * y - 7 and x <= 0 and x >= -7):
        status = "sand"

    match status:
        case "sand": return "Опасность! Покиньте зону как можно скорее!"
        case "water": return "Вы вышли в море и рискуете быть съеденным акулой!"
        case _: return "Зона безопасна. Продолжайте работу."


print(sysDanger(float(input()), float(input())))
