from item import *

class Treasure():
    def __init__(self, posx, posy, health, locked, symbol, helditem):
        self.x = posx
        self.y = posy
        self.health = health
        self.locked = locked
        self.symbol = symbol
        self.item = helditem
        self.open = False
    
    def tryOpen(self):
        if self.locked == False:
            self.open = True
        if self.locked == True:
            print("This chest is locked, attack to open!")

    def giveItem(self, player):
        if self.open == True:
            print("You found an item!")
            print("Use or Discard?")
            choice = input("Input: ")
            if choice.upper() == "USE":
                self.item.use(player)
            else:
                print("You discarded the item")

    def update(self):
        if self.health <= 0:
            self.open = True
        

