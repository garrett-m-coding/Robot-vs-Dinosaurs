from dino import Dinosaur

class Herd:
    def __init__(self):
        self.dinos_list = []
        self.create_herd()
        pass

    def create_herd(self):
        dino1 = Dinosaur('Compsognathus', 10, 50)
        dino2 = Dinosaur('Pterodactyl', 20,100) 
        dino3 = Dinosaur('Velociraptor', 30, 150)
        # dino4 = Dinosaur('Allosaurus', 40, 200)
        # dino5 = Dinosaur('Spinosaurus', 50, 300)
        # dino6 = Dinosaur('Tyrannosaurus Rex', 60, 400)

        self.dinos_list.append(dino1)
        self.dinos_list.append(dino2)
        self.dinos_list.append(dino3)
        # self.dinos_list.append(dino4)
        # self.dinos_list.append(dino5)
        # self.dinos_list.append(dino6)
        pass