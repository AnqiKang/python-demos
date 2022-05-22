# instance method: a function that belongs to an object
# all instance method must take self as the first parameter
class Pokemon():
    def __init__(self, name, specialty, health=100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaaaar!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} pokeman!")

    def take_damage(self, amount):
        self.health = self.health - amount



squirtle = Pokemon("Ssquirtle", "Water")
charmander = Pokemon(name="Charmander", specialty="Fire", health=110)
squirtle.roar()
charmander.roar()

squirtle.describe()
squirtle.take_damage(10)
print(squirtle.health)

