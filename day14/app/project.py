import os
import ctypes

FILE_NAME = "book.csv"


def popup(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def create_data():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w"):
            pass


def add_book():
    title = input("Enter your title: ").strip().title()
    author = input("Enter your author: ").strip().title()
    year = input("Enter your year: ").strip()

    with open(FILE_NAME, "a") as fo:
        fo.write(f"{title},{author},{year},Not Read\n")

    popup("Add Book", "Succesful add book", 0)


def find_book():
    reading_list = get_book()
    match_book = []

    search_book = input("Enter your book to search: ").strip().lower()

    for book in reading_list:
        if search_book in book["title"].lower():
            match_book.append(book)

    return match_book


def get_book():
    books = []

    with open(FILE_NAME) as reading_list:
        for book in reading_list:
            title, author, year, status = book.strip().split(",")

            books.append({
                'title': title,
                'author': author,
                'year': year,
                'status': status
            })

    return books


def show_books(books):
    print()

    for book in books:
        print(f"{book['title']} ({book['year']}) by {book['author']} - {book['status']}")

    print()


def write_books(book_list):
    with open(FILE_NAME, "w") as fo:
        for book in book_list:
            new_book = ",".join(book.values())
            fo.write(new_book + "\n")


def mark_book():
    reading_list = get_book()
    mark_title = input("Enter your title for mark book: ").strip().lower()

    for book in reading_list:
        if mark_title in book['title'].lower():
            book['status'] = "Read"

    write_books(reading_list)


def delete_book():
    reading_list = get_book()
    deleted_title = input("Enter your title to delete book: ").strip().lower()

    ans = []

    for book in reading_list:
        if deleted_title not in book['title'].lower():
            ans.append(book)
    write_books(ans)

    popup("Delete Book", "Deleted Book", 0)


create_data()

menu = """
"a" to add book
"l" to display list book
"s" to search book
"m" to mark book
"d" to delete book
"q" to quit book

Enter character to continue: """

selection = input(menu).strip().lower()

while selection != "q":
    if selection == "a":
        add_book()
    elif selection == "l":
        reading_list = get_book()
        if reading_list:
            show_books(reading_list)
        else:
            print("Your list is empty.")
    elif selection == "s":
        match_book = find_book()
        if match_book:
            show_books(match_book)
        else:
            print()
            print("No book in list")
    elif selection == "m":
        mark_book()
    elif selection == "d":
        delete_book()
    else:
        print("Invalid options !")

    selection = input(menu).strip().lower()
