# Bài 1: Tính S(n) = 1 + 2 + 3 + … + n
"""
input: n (int) > 0
output: S(n)

example:
n = 4
S(4) = 1 + 2 + 3 + 4 = 10

range(1, n+1)
"""
n = int(input('n = '))

t = 0

for i in range(1, n+1):
    t += i

print(f"s({n}) = {t}")

"""
S = n * (n+1) // 2
"""
