from robot import Robot

class Fleet:
    def __init__(self):
        self.robots_list = []
        self.creat_fleet()

    def create_fleet(self):
        robot1 = Robot('Quickest')
        robot2 = Robot('Slowest')
        robot3 = Robot('Balanced')

        self.robots_list.append(robot1)
        self.robots_list.append(robot2)
        self.robots_list.append(robot3)