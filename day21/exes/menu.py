import book_action as ba
def menu():
    ba.create_book_table()
    user_input = input(ba.USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            ba.prompt_add_book()
        elif user_input == 'l':
            ba.list_books()
        elif user_input == 'r':
            ba.prompt_read_book()
        elif user_input == 'd':
            ba.prompt_delete_book()

        user_input = input(ba.USER_CHOICE)