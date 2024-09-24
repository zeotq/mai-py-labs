data = int(input())
s = 0

while data != 0:
    s += data % 10
    data //= 10

print(s)