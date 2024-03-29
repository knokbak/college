#FIRE TYPE PoKEMON
from Pokemon import Pokemon

class Fire_Pokemon(Pokemon):
    def __init__(self, name):
        Pokemon.__init__(self, name, "fire")

    def attack(self, opponent):
        print(f"{self.name} does firey things to {opponent.name}")

        damage = 10
        match opponent.type:
            case "grass":
                damage = 20
            case "water":
                damage = 5
        
        opponent.take_damage(damage)
