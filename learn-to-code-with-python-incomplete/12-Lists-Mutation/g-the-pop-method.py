# pop(): Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
action_stars = ["Norris", "Seagal", "Van Damme", "Schwarzenegger"]
last_action_hero = action_stars.pop()
print(last_action_hero)
print(action_stars)

# pop(index)
second_star = action_stars.pop(1)
print(second_star)
print(action_stars)

action_stars.pop(-1)
print(action_stars)


