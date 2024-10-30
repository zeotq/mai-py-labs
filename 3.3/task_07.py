numbers = {1, 2, 3, 4, 5}
{1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}
res = {i: [j for j in range(1, i + 1) if i % j == 0] for i in numbers}
print(res)