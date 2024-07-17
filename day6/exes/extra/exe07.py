# Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1

"""
input: n (int) > 0

output: S(n)

n = 4

S(4) = 1/2 + 2/3 + 3/4 + 4/5 = 2.72
"""

n = int(input("n = "))

t = 0

for i in range(1, n + 1):
    t += i / (i + 1)

print(f"S({n}) = {t:.2f}")
