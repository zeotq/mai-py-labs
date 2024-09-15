n = [int(input()) for i in range(3)]
print("YES" if all([2 * i < sum(n) for i in n]) else "NO")