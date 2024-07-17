movies = [
    ("Phim Hai", "Tran Thanh", "2023", "$1,000,000")
]

title = input("Enter the title: ")
director = input("Enter the director: ")
release_year = input("Enter the release year: ")
budget = input("Enter the budget: ")

new_movie = title, director, release_year, budget

print(f"{new_movie[0]} ({new_movie[2]})")

movies.append(new_movie)

print(movies[0])
print(movies[1])

# del movies[0]
# first_movie = movies[0]
# movies.remove(first_movie)
print(movies.pop(0))
print(movies)
