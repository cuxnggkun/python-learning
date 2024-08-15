from operator import methodcaller

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
new_names = [name for name in names if len(name) < 8]
ans = map(methodcaller("title"), new_names)

print(*ans, sep=', ')
