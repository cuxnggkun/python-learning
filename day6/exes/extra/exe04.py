# Tính S(n) = ½ + ¼ + … + 1/2n

"""
input: n (int) > 0

output: S(n)
n = 4

S(4) = 1/2 + 1/4 + 1/6 + 1/8 = 1.04


"""

n = int(input("n = "))

t = 0

for i in range(2, 2 * n + 1, 2):
    t += 1 / i

print(f"S({n}) = {t:.2f}")
