from itertools import permutations
a = [i[0] + i[1] for i in sorted(list(permutations(input(), 2)), 
                                 key=lambda k: int(k[0] + k[1])) if i[0] != '0']
print(a[0], a[-1])