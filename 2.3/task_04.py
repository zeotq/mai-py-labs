a, b = [int(input()) for i in range(2)]
c = 1 if a <= b else -1
print(*range(a, b + c, c))