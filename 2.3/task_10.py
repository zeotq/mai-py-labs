x, y = 0, 0
while (dir := input()) != "СТОП":
    tr = int(input())
    match dir:
        case "СЕВЕР": y += tr
        case "ЮГ": y -= tr
        case "ВОСТОК": x += tr
        case "ЗАПАД": x -= tr
        case _: pass
print(y, x, sep="\n")