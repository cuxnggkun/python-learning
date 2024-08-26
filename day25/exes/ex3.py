import random

num1s = sorted(random.sample(range(1, 101), k=15), reverse=True)[:5]
num2s = sorted(random.sample(range(1, 101), k=15), reverse=True)[:5]
num3s = sorted(random.sample(range(1, 101), k=15), reverse=True)[:5]

print(num1s)
print(num2s)
print(num3s)
