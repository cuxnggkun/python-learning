# Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)

"""
input: n (int) > 0

output: S(n)

n = 4

S(4) = 1 + 1/3 + 1/5 + 1/7 + 1/9 = 1.79


"""

n = int(input("n = "))

t = 0

for i in range(1, 2 * n + 2, 2):
    t += 1 / i

print(f"S({n}) = {t:.2f}")
