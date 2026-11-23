class Warrior:
    def __init__ (self, health = 50, attack = 7):
        self.health = health
        self.attack = attack
        if health > 0:
            self.isalive = True
        else:
            self.isalive = False

    def __str__(self):
        return f"Health: {self.health}, attack: {self.attack}, is alive {self.isalive}"
class Knight(Warrior):
    def __init__(self, health = 50, attack = 7):
        super().__init__(health, attack)

Jozo = Warrior()
Zuza = Knight()
print(Jozo)
print(Zuza)