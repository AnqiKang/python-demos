# polymorphism plays well with a subclass hierarchy
import random


class Player():
    def __init__(self, game_played, victories):
        self.game_played = game_played
        self.victories = victories

    @property
    def win_ration(self):
        return self.victories / self.game_played


class Human(Player):
    def make_move(self):
        print("Let player make the decision!")


class Computer(Player):
    def make_move(self):
        print("Run advanced algorithm to calculate best move!")


hp = Human(30, 15)
cp = Computer(1000, 999)
print(hp.win_ration)
print(cp.win_ration)

game_players = [hp, cp]
starting_player = random.choice(game_players)
starting_player.make_move() 
