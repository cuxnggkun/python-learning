# Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2

"""
input: n (int) > 0

output: S(n)

n = 4

S(4) = 1/2 + 3/4 + 5/6 + 7/8 + 9/10 = 3.86
"""
n = int(input("n = "))

t = 0

for i in range(0, n + 1):
    t += (2 * i + 1) / (2 * i + 2)

print(f"S({n}) = {t:.2f}")
