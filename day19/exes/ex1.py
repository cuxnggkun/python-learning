try:
    grades_input = input("Enter grades: ").strip().split(",")

    print([int(x) for x in grades_input])
except Exception as e:
    print(e)
