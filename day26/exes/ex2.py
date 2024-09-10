from collections import defaultdict, Counter

s = "abcaabcd"

# count = defaultdict(int)

# for ch in s:
#     count[ch] += 1

# print(max(count, key=lambda key: count[key]))

counter = Counter(s)

print(counter.most_common(1)[0][0])
