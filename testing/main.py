nums = [2, 2, 1, 1, 1, 2, 2]

ans = cnt = 0

for n in nums:
    if cnt == 0:
        ans = n

    if ans == n:
        cnt += 1
    else:
        cnt -= 1

print(ans)
