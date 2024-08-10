import json
import ctypes

FILE_NAME = "book.json"


def popup(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def create_data():
    try:
        with open("book.json", mode='x') as fo:
            json.dump([], fo)
    except FileExistsError:
        pass


def get_books():
    with open(FILE_NAME) as fp:
        books = json.load(fp)
    return books


def write_books(book_list):
    with open(FILE_NAME, "w") as fo:
        json.dump(book_list, fo, indent=4)


def add_book():
    books = get_books()

    title = input("Enter your title: ").strip().title()
    author = input("Enter your author: ").strip().title()
    year = input("Enter your year: ").strip()

    book = {
        "title": title,
        "author": author,
        "year": year,
        "status": False
    }

    books.append(book)
    write_books(books)

    popup("Add Book", "Succesful add book", 0)


def find_book():
    reading_list = get_books()
    match_book = []

    search_book = input("Enter your book to search: ").strip().lower()

    for book in reading_list:
        if search_book in book["title"].lower():
            match_book.append(book)

    return match_book


def show_books(books):
    print()

    for book in books:
        print(f"{book['title']} ({book['year']}) by {book['author']} - {book['status']}")

    print()


def mark_book():
    reading_list = get_books()
    mark_title = input("Enter your title for mark book: ").strip().lower()

    for book in reading_list:
        if mark_title in book['title'].lower():
            book['status'] = True

    write_books(reading_list)


def delete_book():
    reading_list = get_books()
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
        reading_list = get_books()
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
