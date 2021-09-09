from typing_extensions import ParamSpecKwargs
from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass
    
    def display_welcome(self):
        print('Welcome to Dinos vs Robots Battlefield')
        pass

    def battle(self):
        pass

    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        pass
