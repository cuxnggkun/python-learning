def check_prime(dividend):
    for num in range(2, dividend):
        if dividend % num == 0:
            return False
    else:
        return True

print(check_prime(2))