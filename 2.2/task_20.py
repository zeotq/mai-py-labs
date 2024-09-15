road = sorted(list(filter(lambda a: "зайка" in a, 
                          [input() for i in range(3)])))[0]
print(road, len(road))