from dino import Dinosaur

class Herd:
    def __init__(self, dinosaurs):
        self.dinos_list = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur('pterodactyl', 25, 150)
        dino2 = Dinosaur('tyrannosaurus rex', 75, 450) 
        dino3 = Dinosaur('velociraptor', 25, 150)
        dino4 = Dinosaur('compsognathus', 5, 30)
        dino5 = Dinosaur('allosaurus', 50, 300)
        dino6 = Dinosaur('spinosaurus', 50, 300)

        self.dinos_list.append(dino1)
        self.dinos_list.append(dino2)
        self.dinos_list.append(dino3)
        self.dinos_list.append(dino4)
        self.dinos_list.append(dino5)
        self.dinos_list.append(dino6)