# remove(): rRemove an element from a set; it must be a member.
# If the element is not a member, raise a KeyError.
agents = { "Mulder", "Scully", "Doggett", "Reyes" }

agents.remove("Doggett")
print(agents)

# agents.remove("Skinner") --> KeyError: 'Skinner'

# discard(): Remove an element from a set if it is a member.
# If the element is not a member, do nothing.
agents.discard("Reyes")
print(agents)

agents.discard("Skinner")
print(agents)


