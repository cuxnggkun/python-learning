# Tính S(n) = 1/1×2 + 1/2×3 +…+ 1/n x (n + 1)

"""
input: n (int) > 0


output: S(n)

n = 4

S(4) = 1/2 + 1/6 + 1/12 + 1/20 = 0.8
"""
n = int(input("n = "))

t = 0

for i in range(1, n + 1):
    t += 1 / (i * (i + 1))

print(f"S({n}) = {t:.2f}")
