data = []
while (s := input()) != "Приехали!":
    data.append(s)
print(len(list(filter(lambda a: "зайка" in a, data))))