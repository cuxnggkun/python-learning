movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

num_movies = int(input("How many movie you want add: "))

for _ in range(num_movies):
    movie_name = input("Enter you movie name: ")
    movie_budget = int(input("Enter your movie budget: "))
    new_movie = (movie_name, movie_budget)
    movies.append(new_movie)

total_budget = 0

for movie in movies:
    total_budget += movie[1]

avarage = total_budget / len(movies)

print(avarage)

counters = 0

for movie in movies:
    if movie[1] > avarage:
        print(movie[0])
        counters += 1
print(f"Amount movie higher avarage budget: {counters}")
