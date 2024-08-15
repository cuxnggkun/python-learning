import matplotlib.pyplot as plt
import data_storage as ds
import graphing as gp

select_option = """Enter
"c" to change y data
"q" to quit
What you want to do?  """


def create_chart():
    colum = int(input("Please choose colum: "))
    file_name = input("Please enter file name: ")

    x_data = ds.read_colum(-1)
    y_data = ds.read_colum(colum)

    gp.handle_chart(x_data, y_data, file_name)


def menu():
    while True:
        option = input(select_option)

        if option == "c":
            create_chart()
        elif option == 'q':
            break
        else:
            print("Invalid input!")


if __name__ == '__main__':
    menu()
