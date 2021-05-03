class Creature():
    def __init__(self, posx, posy, health, damage, state, symbol):
        self.x = posx
        self.y = posy
        self.health = health
        self.damage = damage
        self.state = state
        self.symbol = symbol
        self.alive = True

    def attack(self, player):
        player.health -= self.damage

    def update(self):
        if self.health <= 0:
            self.alive = False

    def interact(self, player):
        if self.state == True:
            player.health -= self.damage
            print("The creature was hostile and attacked you for " + str(self.damage) + " damage!")
        if self.state == False:
            print("The creature looks at you and runs away")
            print("You restored 5 health!")
            player.health += 5
            self.alive = False
            self.update()
        else:
            pass