for divided in range(2,101):
    for num in range(2, divided):
        if divided % num == 0:
            print(f"This {divided} is not the prime")
            break
    else:

        print(f"This {divided} is prime number ")
