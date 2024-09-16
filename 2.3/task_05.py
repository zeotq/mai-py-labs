paycheck = 0
while (price := float(input())) != 0:
    paycheck += price * 0.9 if price >= 500 else price
print(paycheck)