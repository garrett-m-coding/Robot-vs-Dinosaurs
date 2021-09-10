from weapon import Weapon

class Robot:
    def __init__(self, name, health, Weapon):
        self.name = name
        self.health = health
        self.weapon = Weapon
        pass

    def robot_attack(self, dinosaur):
        # robot attacks dinosaur
        # this method addresses specific dinosaur
        # and decreases that specific dinosaur's health
        # decreases health by specific robo's attack power
        dinosaur.health -= self.Weapon.attack_power
        pass