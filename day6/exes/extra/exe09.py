# Bài 9: Tính T(n) = 1 x 2 x 3…x N
"""
input: n (int) > 0

output: T(n)

n = 4

T(4) = 1 x 2 x 3 x 4 = 24
"""
n = int(input("n = "))

t = 1

for i in range(1, n + 1):
    t *= i

print(f"T({n}) = {t}")
