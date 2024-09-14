players = ["Петя", "Вася", "Толя"]
velocity = [(players[i], int(input())) for i in range(3)]
for i, el in enumerate(sorted(velocity, key=lambda a: a[1], reverse=True)):
    print(f'{i + 1}. {el[0]}')