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
        self.display_winner()
        pass

    def display_welcome(self):
        print(f"Welcome to {self.name}! Are you rooting for the Dinos' natural strength or the Robots' intelligence?")
        pass

    def battle(self):
        self.dino_turn1()
        self.robo_turn1()
        self.dino_turn2()
        self.robo_turn2()
        self.dino_turn3()
        self.robo_turn3()
        self.dino_turn4()
        self.robo_turn4()
        self.dino_turn5()
        self.robo_turn5()
        self.dino_turn6()
        self.robo_turn6()
        self.dino_turn7()
        self.robo_turn7()
        self.dino_turn8()
        self.robo_turn8()
        self.dino_turn9()
        self.robo_turn9()
        pass
        # while dino health is above 0, attack Robot
        # while robo health is above 0, attack Dinosaur
        # when dino health is less than or equal to 0, delete dino from dino list
        # when robo health is less than or equal to 0, delete robo from robo list
        # alternate attacks between dino and robo until all of robos/dinos health is depleted
        # can't figure out how to make the battles alternate with a while/for loop and if conditionals?!

    def dino_turn1(self):
        print(f"Robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        self.herd.dinos_list[0].dino_attack(self.fleet.robos_list[0])
        print(f"After {self.herd.dinos_list[0].name}'s attack, robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        pass

    def robo_turn1(self):
        print(f"Dinosaur {self.herd.dinos_list[0].name}'s health is: {self.herd.dinos_list[0].health}.")
        self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[0])
        print(f"After {self.fleet.robos_list[0].name}'s attack, dinosaur {self.herd.dinos_list[0].name}'s health is: {self.herd.dinos_list[0].health}.")
        pass

    def dino_turn2(self):
        print(f"Robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        self.herd.dinos_list[0].dino_attack(self.fleet.robos_list[0])
        print(f"After {self.herd.dinos_list[0].name}'s attack, robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        pass

    def robo_turn2(self):
        print(f"Dinosaur {self.herd.dinos_list[0].name}'s health is: {self.herd.dinos_list[0].health}.")
        self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[0])
        print(f"After {self.fleet.robos_list[0].name}'s attack, dinosaur {self.herd.dinos_list[0].name}'s health is: {self.herd.dinos_list[0].health}. {self.herd.dinos_list[0].name} is dead.")
        # remove dino [0] because dead
        pass
    
    def dino_turn3(self):
        print(f"Robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        self.herd.dinos_list[1].dino_attack(self.fleet.robos_list[0])
        print(f"After {self.herd.dinos_list[1].name}'s attack, robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        pass

    def robo_turn3(self):
        print(f"Dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[1])
        print(f"After {self.fleet.robos_list[0].name}'s attack, dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        pass

    def dino_turn4(self):
        print(f"Robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}.")
        self.herd.dinos_list[1].dino_attack(self.fleet.robos_list[0])
        print(f"After {self.herd.dinos_list[1].name}'s attack, robot {self.fleet.robos_list[0].name}'s health is: {self.fleet.robos_list[0].health}. {self.fleet.robos_list[0].name} is dead.")
        # remove rovo [0] because dead
        pass

    def robo_turn4(self):
        print(f"Dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        self.fleet.robos_list[1].robot_attack(self.herd.dinos_list[1])
        print(f"After {self.fleet.robos_list[1].name}'s attack, dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        pass

    def dino_turn5(self):
        print(f"Robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}.")
        self.herd.dinos_list[1].dino_attack(self.fleet.robos_list[1])
        print(f"After {self.herd.dinos_list[1].name}'s attack, robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}.")
        pass

    def robo_turn5(self):
        print(f"Dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        self.fleet.robos_list[1].robot_attack(self.herd.dinos_list[1])
        print(f"After {self.fleet.robos_list[1].name}'s attack, dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        pass

    def dino_turn6(self):
        print(f"Robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}.")
        self.herd.dinos_list[1].dino_attack(self.fleet.robos_list[1])
        print(f"After {self.herd.dinos_list[1].name}'s attack, robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}.")
        pass

    def robo_turn6(self):
        print(f"Dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}.")
        self.fleet.robos_list[1].robot_attack(self.herd.dinos_list[1])
        print(f"After {self.fleet.robos_list[1].name}'s attack, dinosaur {self.herd.dinos_list[1].name}'s health is: {self.herd.dinos_list[1].health}. {self.herd.dinos_list[1].name} is dead.")
        # remove dino [1] because dead
        pass

    def dino_turn7(self):
        print(f"Robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}.")
        self.herd.dinos_list[2].dino_attack(self.fleet.robos_list[1])
        print(f"After {self.herd.dinos_list[2].name}'s attack, robot {self.fleet.robos_list[1].name}'s health is: {self.fleet.robos_list[1].health}. {self.fleet.robos_list[1].name} is dead.")
        # remove robo [1] because dead
        pass

    def robo_turn7(self):
        print(f"Dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}.")
        self.fleet.robos_list[2].robot_attack(self.herd.dinos_list[2])
        print(f"After {self.fleet.robos_list[2].name}'s attack, dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}.")
        pass

    def dino_turn8(self):
        print(f"Robot {self.fleet.robos_list[2].name}'s health is: {self.fleet.robos_list[2].health}.")
        self.herd.dinos_list[2].dino_attack(self.fleet.robos_list[2])
        print(f"After {self.herd.dinos_list[2].name}'s attack, robot {self.fleet.robos_list[2].name}'s health is: {self.fleet.robos_list[2].health}.")
        pass

    def robo_turn8(self):
        print(f"Dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}.")
        self.fleet.robos_list[2].robot_attack(self.herd.dinos_list[2])
        print(f"After {self.fleet.robos_list[2].name}'s attack, dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}.")
        pass

    def dino_turn9(self):
        print(f"Robot {self.fleet.robos_list[2].name}'s health is: {self.fleet.robos_list[2].health}.")
        self.herd.dinos_list[2].dino_attack(self.fleet.robos_list[2])
        print(f"After {self.herd.dinos_list[2].name}'s attack, robot {self.fleet.robos_list[2].name}'s health is: {self.fleet.robos_list[2].health}.")
        pass

    def robo_turn9(self):
        print(f"Dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}.")
        self.fleet.robos_list[2].robot_attack(self.herd.dinos_list[2])
        print(f"After {self.fleet.robos_list[2].name}'s attack, dinosaur {self.herd.dinos_list[2].name}'s health is: {self.herd.dinos_list[2].health}. {self.herd.dinos_list[2].name} is dead.")
        # remove dino [2] because dead
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winner(self):
        print("All dinosaurs have died, while one robot survives. Robots are victorious!!!")
        pass

####################################################################################################

        # while self.fleet.robos_list[0].health >= 0:
        #     if self.herd.dinos_list[0].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[0])
        #     if self.herd.dinos_list[1].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[1])
        #     if self.herd.dinos_list[2].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[2])
        #     if self.herd.dinos_list[3].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[3])
        #     if self.herd.dinos_list[4].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[4])        
        #     if self.herd.dinos_list[5].health >= 0:
        #         self.fleet.robos_list[0].robot_attack(self.herd.dinos_list[5])

        # while self.fleet.robos_list[1].health >= 0:
        #     if self.herd.dinos_list[1].health >= 0:
        #         self.fleet.robos_list[1].robot_attack(self.herd.dinos_list[1])

        # while self.fleet.robos_list[2].health >= 0:
        #     if self.herd.dinos_list[2].health >= 0:
        #         self.fleet.robos_list[2].robot_attack(self.herd.dinos_list[2])

        # while self.fleet.robos_list[3].health >= 0:
        #     if self.herd.dinos_list[3].health >= 0:
        #         self.fleet.robos_list[3].robot_attack(self.herd.dinos_list[3])        

        # while self.fleet.robos_list[4].health >= 0:
        #     if self.herd.dinos_list[4].health >= 0:
        #         self.fleet.robos_list[4].robot_attack(self.herd.dinos_list[4])

        # while self.fleet.robos_list[5].health >= 0:
        #     if self.herd.dinos_list[5].health >= 0:
        #         self.fleet.robos_list[5].robot_attack(self.herd.dinos_list[5])