n, m, t = [int(input()) for i in range(3)]  # hours, minutes, delive time
time = (n * 60 + m + t) % 1440              # time after delive 
time_hours = time // 60
time_minutes = time % 60

print(f"{time_hours if time_hours >= 10 else f'0{time_hours}'}:" +
      f"{time_minutes if time_minutes >= 10 else f'0{time_minutes}'}")