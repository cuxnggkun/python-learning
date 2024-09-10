from collections import namedtuple


Movie = namedtuple("Movie", ["title", "director", "year", "budget"])

movie_obj = Movie(
    title=input('Enter title: ').title().strip(),
    director=input('Enter director: ').title().strip(),
    year=int(input('Enter year of release: ')),
    budget=int(input('Enter budget: '))
)

print(f"{movie_obj.title} by {movie_obj.director} - {movie_obj.year} earned {movie_obj.budget}$")
