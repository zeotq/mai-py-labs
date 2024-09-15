numbers = [int(input()) for i in range(3)]
print(numbers[0] % 10 if numbers[0] % 10 == numbers[1] % 10 
      and numbers[1] % 10 == numbers[2] % 10
      else numbers[0] // 10)