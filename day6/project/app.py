for number in range(1, 101):
    # if number % 15 == 0:
    #     print("Fizz Buzz")
    # elif number % 3 == 0:
    #     print("Fizz")
    # elif number % 5 == 0:
    #     print("Buzz")
    # else:
    #     print(number)

    div3 = (number % 3 == 0) * 'Fizz'
    div5 = (number % 5 == 0) * 'Buzz'
    div35 = div3 + div5
    print(div35 or number)
