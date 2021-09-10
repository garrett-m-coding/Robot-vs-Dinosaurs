from weapon import Weapon
from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.create_fleet()
        pass

    def create_fleet(self):
        robot1a = Robot('Speedbot A', 50, Weapon('machine gun', 25))
        robot1b = Robot('Speedbot B', 50, Weapon('machine gun', 25))
        robot2a = Robot('Slowbot A', 150, Weapon('bazooka', 100))
        robot2b = Robot('Slowbot B', 150, Weapon('bazooka', 100))
        robot3a = Robot('Balanced Bot A', 100, Weapon('.50 caliber', 50))
        robot3b = Robot('Balanced Bot B', 100, Weapon('.50 caliber', 50))

        self.robots_list.append(robot1a)
        self.robots_list.append(robot1b)
        self.robots_list.append(robot2a)
        self.robots_list.append(robot2b)
        self.robots_list.append(robot3a)
        self.robots_list.append(robot3b)
        pass