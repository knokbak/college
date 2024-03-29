#Pokemon Class

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.__health = 80
    
    def whoamI(self):
        print(f"Hello, I am {self.name}")
    
    def attack(self, opponent):
        print (f"{self.name} attacks {opponent.name}")
        opponent.take_damage(10)

    def take_damage(self, amount):
        print (f"Oof! That attack hurt {self.name}")
        self.__health -= amount
        if self.__health <= 0:
            self.murder()
    
    def murder(self):
        self.__health = 0
        print(f"Oh noes!! {self.name} was murdered!!")








