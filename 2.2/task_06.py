year = int(input())
# Условия високосного года по Григорианскому календарю
print("YES" if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0 
      else "NO")