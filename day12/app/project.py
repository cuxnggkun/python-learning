reading_list = []

menu = """
--------------------------
"a" to add book
"l" to display list
"q" to quit the menu
--------------------------
Please enter character to continue: """

selection = input(menu).strip().lower()


def add_book():
    title = input("Please enter title: ").strip().title()
    author = input("Please enter author: ").strip().title()
    year = input("Please enter year of realese: ").strip()

    new_list = {
        'title': title,
        'author': author,
        'year': year
    }

    reading_list.append(new_list)
    print("Added book.")


def show_book():
    for book in reading_list:
        title, author, year = book.values()
        print(f"{title} ({year}) by {author}")
        print("Displayed list.")


while selection != "q":
    if selection == "a":
        add_book()
    elif selection == "l":
        if reading_list:
            show_book()
        else:
            print("List is empty")
    else:
        print(f"Invalid {selection} option ! ")

    selection = input(menu).strip().lower()
