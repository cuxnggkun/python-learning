def add(add1, add2):
    result1 = add1 + add2
    print("Add: ", result1)


def subtract(sub1, sub2):
    result2 = sub1 - sub2
    print("Subtract: ", result2)


def divide(div1, div2):
    if div2 == 0:
        print("Warning! Do not enter 0 in divide !")
    else:
        result3 = div1 / div2
        print("Divide: ", result3)


def multiply(multi1, multi2):
    result4 = multi1 * multi2
    print("Multiply: ", result4)


add(1, 2)
subtract(6, 2)
divide(10, 0)
multiply(5, 2)
