def ex2():
    try:
        1 / 0
        return "try"
    except:
        return "except"
    finally:
        return "finally"


print(ex2())
