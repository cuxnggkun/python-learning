movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie_info = {
    key.title(): value.title() for key, value in movie.items()
}

print(movie_info)
