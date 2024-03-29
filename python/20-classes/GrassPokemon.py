#GRASS TYPE PoKEMON
from Pokemon import Pokemon

class Grass_Pokemon(Pokemon):
    def __init__(self, name):
        Pokemon.__init__(self, name, "grass")

    def attack(self, opponent):
        print(f"{self.name} does grass stuff or something like that with {opponent.name} ??")

        damage = 10
        match opponent.type:
            case "fire":
                damage = 5
            case "water":
                damage = 20
        
        opponent.take_damage(damage)
    
