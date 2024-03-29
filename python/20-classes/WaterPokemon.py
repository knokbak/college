#WATER TYPE PoKEMON
from Pokemon import Pokemon

class Water_Pokemon(Pokemon):
    def __init__(self, name):
        Pokemon.__init__(self, name, "water")

    def attack(self, opponent):
        print(f"{self.name} literally just drowned {opponent.name}")

        damage = 10
        match opponent.type:
            case "fire":
                damage = 5
            case "grass":
                damage = 20
        
        opponent.take_damage(damage)
        
    
