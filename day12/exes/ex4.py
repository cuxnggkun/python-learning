def check_palindrome(words):
    words = words.strip().lower()
    reversed_word = reversed(words)

    if list(words) == list(reversed_word):
        print(True)
    else:
        print(False)


check_palindrome("khok")

