# Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2

"""
input: n int() > 0

output: S(n)

example:
n = 4
S(4) = 1^2 + 2^2 + 3^2 + 4^2 = 30

"""
n = int(input("n = "))

t = 0

for i in range(1, n + 1):
    t += i ** 2

print(f"S({n}) = {t}")
