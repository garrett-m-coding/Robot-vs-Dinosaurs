class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        pass

    def dino_attack(self, robot):
        # dino attacks robot
        # this method addresses specific robot
        # and decreases that specific robot's health
        # decreases health by specific dino's attack power
        robot.health -= self.attack_power
        pass