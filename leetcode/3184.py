def countCompleteDayPairs(hours):
    count = 0
    for i in range(len(hours)):
        for j in range(i + 1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                count += 1
    return count


print(countCompleteDayPairs([12, 12, 30, 24, 24]))
