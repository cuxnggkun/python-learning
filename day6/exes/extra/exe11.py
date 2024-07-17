# Bài 11: Tính S(n) = 1 + 1.2 + 1.2.3 + … + 1.2.3….N

"""
input: n (int) > 0

output: S(n)
n = 4

S(4) = 1 + 1*2 + 1*2*3 + 1*2*3*4 = 33
"""
n = int(input("n = "))

s = 0
t = 1

for i in range(1, n + 1):
    t *= i
    s += t

print(f"S({n}) = {s}")
