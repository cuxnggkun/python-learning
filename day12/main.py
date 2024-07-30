#    012345
s = "ABCDCDC"
sub = "CDC"

c = 0

for i in range(0, len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        c += 1

print(c)
