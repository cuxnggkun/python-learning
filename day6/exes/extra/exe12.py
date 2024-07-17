# Bài 12: Tính S(n) = x + x^2 + x^3 + … + x^n
"""
input: n (int) > 0
x (float)
output: S(n)

n = 4
x = 2.0

S(4) = 2 + 2**2 + 2**3 + 2**4 = 30
"""
n = int(input("n = "))
x = float(input("x = "))

s = 0

for i in range(1, n + 1):
    s += x ** i

print(f"S({n}) = {s}")
