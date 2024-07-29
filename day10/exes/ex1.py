describe_album =  (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )

keys = ("album name", "the band", "year of release", "track list")

# album = {}
#
# for i in range(len(keys)):
#     album[keys[i]] = describe_album[i]
#
# print(album)

print(dict(zip(keys, describe_album)))
