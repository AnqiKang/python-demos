# add key-value pairs
sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Maning", "Odell Beckham"]
}

sports_team_rosters["Pittsburgh Steelers"] = [
    "Ben Roethlisberger", "amypmop Brown"]
print(sports_team_rosters)

# overwrite
sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger"]
print(sports_team_rosters)

# create, add, update/overwrite
video_game_options = {}
video_game_options["subtitle"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volum"] = 7
video_game_options["volum"] = 70
print(video_game_options)

# dynamic key: extract key from another type
words = ["danger", "beware","danger"]
word_dict = {}

for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

print(word_dict)
