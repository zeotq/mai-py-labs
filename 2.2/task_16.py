def winners(n) -> None:
    """Печатает пьедестал с победителями"""

    out = (
           10 * " " + n[0][0] + 10 * " " + "\n" +
           2 * " " + n[1][0] + 2 * " " + "\n" +
           18 * " " + n[2][0] + 2 * " " + "\n" +
           "   II   " + "   I   " + "   III   "
    )
    print(out)


names = ["Петя", "Вася", "Толя"]
speeds = [(names[i], input()) for i in range(3)]
speeds.sort(key=lambda a: int(a[1]), reverse=True)
winners(speeds)