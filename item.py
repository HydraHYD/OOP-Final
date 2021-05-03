class Item():
    def __init__(self, modifier):
        self.modifier = modifier

class attackMod(Item):
    def use(self, player):
        player.damage += self.modifier
        print("You gained " + str(self.modifier) + " damage")

class healthMod(Item):
    def use(self, player):
        player.health += self.modifier
        print("You gained " + str(self.modifier) + " health")

