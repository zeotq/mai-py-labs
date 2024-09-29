data = int(input())
max_element = 0

while data != 0:
    max_element = max(max_element, data % 10)
    data //= 10

print(max_element)