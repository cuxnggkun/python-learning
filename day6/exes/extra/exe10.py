# Bài 10: Tính T(x, n) = x^n

"""
input: n (int) > 0
x (float)
output: T(x,n)

n = 4
x = 2.0

T(2.0, 4) = 2.0^4 = 16
"""
n = int(input("n = "))
x = float(input("x = "))

t = 1

for _ in range(n):
    t *= x

print(f"T({x},{n}) = {t}")

"""
2^4 = 2x2x2x2 = 16
"""
