# define the relative truthiness or falseness of custom objects
from pkg_resources import empty_provider


class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity


emo_state = Emotion(50, 75)

if emo_state:
    print("This will NOT print because I have more negativity than positivity")


emo_state.positivity = 100
if emo_state:
    print("This will print because I have more positivity than negativity")

