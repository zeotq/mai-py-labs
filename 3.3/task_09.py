numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
'1 - 2 - 3 - 4 - 6 - 7 - 10'
res = " - ".join(list(map(str, sorted(list({i for i in numbers})))))
print(res)