from weapon import Weapon

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        pass

    def robot_attack(self, dinosaur):
        # robot attacks dinosaur
        # this method addresses specific dinosaur
        # and decreases that specific dinosaur's health
        # decreases health by specific robo's attack power
        dinosaur.health -= self.weapon.attack_power
        pass