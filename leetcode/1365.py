def smallerNumbersThanCurrent(nums):
    """
    nums = [8,1,2,2,3]
     0  1  2  3  4
    [1, 2, 2, 3, 8]
    """

    numbers = sorted(nums)

    res = {}

    for i in range(len(numbers)):
        if numbers[i] not in res:
            res[numbers[i]] = i

    return [res[n] for n in nums]

print(smallerNumbersThanCurrent([8,1,2,2,3]))