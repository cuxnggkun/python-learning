from string import ascii_letters


def check_ascii(s):
    for ch in s:
        if ch not in ascii_letters:
            return False
    else:
        return True


print(check_ascii(input("Enter a string: ")))
