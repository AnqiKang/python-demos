# set default: if the key doesn't exist,
film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Gooddellas": "Martin Scorses"
}

print(film_directors.get("Goodfellas"))

# get() will not modity the origial dict
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors)

# setdefault(): if the key doen't exist, add it to dict
# if the key exist, nothing will happen
film_directors.setdefault("Bad Boys", "Michael Bay")
print(film_directors)
film_directors.setdefault("Bad Boys", "A good director")
print(film_directors)