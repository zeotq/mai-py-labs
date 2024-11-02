rle = [('a', 2), ('b', 3), ('c', 1)]
'aabbbc'
res = "".join([lit * count for lit, count in rle])
print(res)