n = [int(i) for i in (input() + input())]
print(100 * max(n) + 1 * min(n) + 10 * ((sum(n) - max(n) - min(n)) % 10))