def greet():
    username = input("Please enter your name: ").strip().title()
    print(f"Hello, {username or 'World'}! ")

greet()