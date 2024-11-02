text = 'Мама мыла раму!'
{'а': 4, 'л': 1, 'м': 4, 'р': 1, 'у': 1, 'ы': 1}
res = {i: text.lower().count(i) for i in ''.join(filter(str.isalpha, sorted(text.lower())))}
print(res)
print(''.join(filter(str.isalpha, sorted(text.lower()))))