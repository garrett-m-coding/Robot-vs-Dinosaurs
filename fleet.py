from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.creat_fleet()

    def create_fleet(self):
        robot1 = Robot('Quickest', 30, Weapon('machine gun', 5))
        robot2 = Robot('Slowest', 150, Weapon('bazooka', 25))
        robot3 = Robot('Balanced', 90, Weapon ('.50 caliber', 15))

        self.robots_list.append(robot1)
        self.robots_list.append(robot2)
        self.robots_list.append(robot3)