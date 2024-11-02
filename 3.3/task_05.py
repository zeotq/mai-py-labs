numbers = [number for number in range(16, 100, 4)]
{16, 64, 36}
res = {i for i in numbers if (i ** 0.5).is_integer()}
print(res)