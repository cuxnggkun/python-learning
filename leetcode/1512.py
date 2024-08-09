"""
nums = [1,2,3,1,1,3]
"""

from collections import Counter

nums = [1, 2, 3, 1, 1, 3]

"""
n = 6
5 + 4 + 3 + 2 + 1 = 5 * (5 + 1) // 2 = 15
n * (n - 1) / 2 = n^2 
"""

print(Counter(nums)[1])
