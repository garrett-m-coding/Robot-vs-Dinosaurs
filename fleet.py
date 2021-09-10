from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robos_list = []
        self.create_fleet()
        pass

    def create_fleet(self):
        robot1a = Robot('Speedbot A', 50, (Weapon('machine gun', 25)))
        robot1b = Robot('Speedbot B', 50, (Weapon('machine gun', 25)))
        robot2a = Robot('Balanced Bot A', 100, (Weapon('.50 caliber', 50)))
        # robot2b = Robot('Balanced Bot B', 100, (Weapon('.50 caliber', 50)))
        # robot3a = Robot('Slowbot A', 150, (Weapon('bazooka', 100)))
        # robot3b = Robot('Slowbot B', 150, (Weapon('bazooka', 100)))

        self.robos_list.append(robot1a)
        self.robos_list.append(robot1b)
        self.robos_list.append(robot2a)
        # self.robos_list.append(robot2b)
        # self.robos_list.append(robot3a)
        # self.robos_list.append(robot3b)
        pass