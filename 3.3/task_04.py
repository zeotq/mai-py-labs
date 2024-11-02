numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
{1, 3}
res = {i for i in numbers if i % 2 != 0}
print(res)