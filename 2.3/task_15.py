n = int(input())
wild_hunt = [True if "зайка" in input() else False for i in range(n)]
print(wild_hunt.count(True))