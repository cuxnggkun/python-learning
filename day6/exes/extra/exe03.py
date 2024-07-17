# Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n

"""
input: n (int) > 0

output: S(n)
n = 4

S(4) = 1 + 1/2 + 1/3 + 1/4 = 2,05

"""
n = int(input("n = "))

t = 0

for i in range(1, n + 1):
    t += 1 / i

print(f"S({n}) = {t:.2f}")
