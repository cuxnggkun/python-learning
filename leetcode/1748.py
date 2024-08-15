from collections import Counter


def sumOfUnique(nums):
    total = 0

    # for x in nums:
    #     if nums.count(x) == 1:
    #         total += x
    #

    for num, freq in Counter(nums).items():
        if freq == 1:
            total += num

    return total

print(sumOfUnique([1,1,1,1,1]))
