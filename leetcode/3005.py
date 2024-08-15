from collections import Counter

def maxFrequencyElements(nums):
    counter = Counter(nums)
    max_freq = max(counter.values())
    return sum(x for x in counter.values() if x == max_freq)


print(maxFrequencyElements([1, 2, 2, 3, 1, 4]))
