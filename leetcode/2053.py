def kthDistinct(arr, k):
    count = 0
    lst = {}

    for ch in arr:
        if ch in lst:
            lst[ch] = False
        else:
            lst[ch] = True

    for ch in arr:
        if lst[ch]:
            count += 1
        if count == k:
            return ch

    return ""


print(kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
