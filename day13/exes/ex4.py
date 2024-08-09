def check_prime(dividend):
    if dividend < 2:
        return False

    for num in range(2, dividend):
        if dividend % num == 0:
            return False
    return True


print(check_prime(1))
