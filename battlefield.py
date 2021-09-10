from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet()
        self.herd = Herd()

# start the Battlefield game
    def run_game(self):
        self.display_welcome()
        self.battle()
        pass

    def display_welcome(self):
        print(f"Welcome to {self.name}! Are you rooting for the Dinos' natural strength or the Robots' intelligence?")
        pass

    def battle(self):
        self.dino_turn()
        self.robo_turn()
        pass

    def dino_turn(self):
        print(f"Robot {self.fleet.robots_list[0].name}'s health is: {self.fleet.robots_list[0].health}.")
        self.herd.dinos_list[0].dino_attack(self.fleet.robots_list[0])
        print(f"After {self.herd.dinos_list[0].name}'s attack, robot {self.fleet.robots_list[0].name}'s health is: {self.fleet.robots_list[0].health}.")
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass
