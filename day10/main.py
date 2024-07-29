# dict
d = {}

print(type(d))

d1 = {'a': 100, 'b': 1, 'c': 123}

# print(d1['x'])

print(d1.get('x', 1000))
print(d1.setdefault('x', 1000))
print(d1)

d1['a'] = 1100
d1['w'] = 987
print(d1)

d1.update({'a': 101, 'v': 8, 'u': 90})
d1.update(n=0, m=7)

print(d1)

print(d1.pop('wa', 10000))
print(d1)

# del d1['ui']
# print(d1)

print(d1.popitem())
print(d1)

# d1.clear()
print(d1)

a = [3, 1, 2, 4, 3]
print(dict.fromkeys(a, 100))

print('-' * 20)

for key, value in d1.items():
    print(key, '-', value)
