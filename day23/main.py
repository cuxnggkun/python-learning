from collections import Counter


def repeatedCharacter(s):
    seen = set()

    for char in s:
        if char in seen:
            return char
        else:
            seen.add(char)


print(repeatedCharacter("abcdd"))
