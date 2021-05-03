class Player():
    def __init__(self, vision, x, y, health, damage, symbol):
        self.health = health
        self.damage = damage
        self.vision = vision
        self.x = x
        self.y = y
        self.alive = True
        self.symbol = symbol

    def update(self):
        if self.health <= 0:
            self.alive = False