string = 'открытое акционерное общество'
'ОАО'
res = "".join([i[0].upper() for i in string.split()])
print(res)