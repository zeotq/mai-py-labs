n = [int(i) for i in input()]
print("YES" if 3 * (max(n) + min(n)) == 2 * sum(n) else "NO")