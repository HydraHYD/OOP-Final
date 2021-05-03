from player import *
from gameMap import *
from creature import *
from item import *
from treasure import *
import random as r

fullMap = []
newMap = gameMap(20,20, fullMap)
newPlayer = Player(2, 9, 9, 20, 5, "P")
running = True
numCreatures = 10
numTreasure = 30
numLocked = r.randint(0, numTreasure)
numOpen = numTreasure - numLocked

atkItem = r.randint(0, numTreasure)
hpItem  = numTreasure - atkItem

hostCreatures = r.randint(0, numCreatures)
passiveCreatures = numCreatures - hostCreatures

creatures = []
treasures = []
items = []

for i in range(hostCreatures):
    creatures.append(Creature(r.randint(0,19), r.randint(0,19), r.randint(2,15), r.randint(1,10), True, "C"))

for i in range(passiveCreatures):
    creatures.append(Creature(r.randint(0,19), r.randint(0,19), r.randint(2,15), r.randint(1,10), False, "C"))

for i in range(atkItem):
    items.append(attackMod(r.randint(-3, 3)))

for i in range(hpItem):
    items.append(healthMod(r.randint(-10, 10)))

for i in range(numLocked):
    treasures.append(Treasure(r.randint(0,19), r.randint(0,19), r.randint(2,15), True, "T", items[0]))
    items.pop(0)

for i in range(numOpen):
    treasures.append(Treasure(r.randint(0,19), r.randint(0,19), r.randint(2,15), False, "T", items[0]))
    items.pop(0)

def checkMapItems(creatureList, treasureList):
    for a in creatureList:
        for b in treasureList:
            if a.x == b.x and a.y == b.y:
                a.x += 1

def playerPosition(mapList, player):
    posy = mapList.map[player.y]
    posy[player.x] = player.symbol

def creaturePosition(mapList, player, creatureList):
    for i in creatureList:
        if i.alive == True:
            if i.x == player.x:
                if i.y == player.y:
                    i.x += 1
            posy = mapList.map[i.y]
            posy[i.x] = i.symbol
        if i.alive == False:
            creatureList.remove(i)

def treasurePosition(mapList, player, treasureList):
    for i in treasureList:
        if i.open == False:
            if i.x == player.x:
                if i.y == player.y:
                    i.x += 1
            posy = mapList.map[i.y]
            posy[i.x] = i.symbol
        if i.open == True:
            i.giveItem(newPlayer)
            treasureList.remove(i)

newMap.createMap()

print("Welcome to this short interaction game")
input("Input anything to start!: ")

def update():
    while running == True:
        newMap.clearOld()
        checkMapItems(creatures, treasures)
        playerPosition(newMap, newPlayer)
        creaturePosition(newMap, newPlayer, creatures)
        treasurePosition(newMap, newPlayer, treasures)
        newMap.showMap()
        print("P = Player, C = Creature, T = Treasure")
        print("Health: " + str(newPlayer.health))
        print("Damage: " + str(newPlayer.damage))
        print("Input Left, Right, Up or Down to move")
        print("Input anything else to skip")
        movement = input("Input: ")
        if movement.upper() == "LEFT":
            newPlayer.x -= 1
        if movement.upper() == "RIGHT":
            newPlayer.x += 1
        if movement.upper() == "UP":
            newPlayer.y -= 1
        if movement.upper() == "DOWN":
            newPlayer.y += 1
        else:
            pass
        
        print("Input Attack or Interact")
        action = input("Input: ")
        print("Input Direction (Left, Right, Up or Down)")
        direction = input("Direction: ")
        if action.upper() == "ATTACK":
            if direction.upper() == "LEFT":
                for i in creatures:
                    if i.x == newPlayer.x - 1 and i.y == newPlayer.y:
                        i.health -= newPlayer.damage
                        print("Creature Health Remaining:" + str(i.health))
                        i.update()
                for i in treasures:
                    if i.x == newPlayer.x - 1 and i.y == newPlayer.y:
                        i.health -= newPlayer.damage
                        print("Treasure Health Remaining:" + str(i.health))
                        i.update()
            if direction.upper() == "RIGHT":
                for i in creatures:
                    if i.x == newPlayer.x + 1 and i.y == newPlayer.y:
                        i.health -= newPlayer.damage
                        print("Creature Health Remaining:" + str(i.health))
                        i.update()
                for i in treasures:
                    if i.x == newPlayer.x + 1 and i.y == newPlayer.y:
                        i.health -= newPlayer.damage
                        print("Treasure Health Remaining:" + str(i.health))
                        i.update()
            if direction.upper() == "UP":
                for i in creatures:
                    if i.x == newPlayer.x and i.y == newPlayer.y - 1:
                        i.health -= newPlayer.damage
                        print("Creature Health Remaining:" + str(i.health))
                        i.update()
                for i in treasures:
                    if i.x == newPlayer.x and i.y == newPlayer.y - 1:
                        i.health -= newPlayer.damage
                        print("Treasure Health Remaining:" + str(i.health))
                        i.update()
            if direction.upper() == "DOWN":
                for i in creatures:
                    if i.x == newPlayer.x and i.y == newPlayer.y + 1:
                        i.health -= newPlayer.damage
                        print("Creature Health Remaining:" + str(i.health))
                        i.update()
                for i in treasures:
                    if i.x == newPlayer.x and i.y == newPlayer.y + 1:
                        i.health -= newPlayer.damage
                        print("Treasure Health Remaining:" + str(i.health))
                        i.update()
        if action.upper() == "INTERACT":
            if direction.upper() == "LEFT":
                for i in creatures:
                    if i.x == newPlayer.x - 1 and i.y == newPlayer.y:
                        i.interact(newPlayer)
                            
                for i in treasures:
                    if i.x == newPlayer.x - 1 and i.y == newPlayer.y:
                        i.tryOpen()
                        i.update()
                        i.giveItem(newPlayer)

            if direction.upper() == "RIGHT":
                for i in creatures:
                    if i.x == newPlayer.x + 1 and i.y == newPlayer.y:
                        i.interact(newPlayer)
                for i in treasures:
                    if i.x == newPlayer.x + 1 and i.y == newPlayer.y:
                        i.tryOpen()
                        i.update()
                        i.giveItem(newPlayer)

            if direction.upper() == "UP":
                for i in creatures:
                    if i.x == newPlayer.x and i.y == newPlayer.y - 1:
                        i.interact(newPlayer)
                for i in treasures:
                    if i.x == newPlayer.x and i.y == newPlayer.y - 1:
                        i.tryOpen()
                        i.update()
                        i.giveItem(newPlayer)

            if direction.upper() == "DOWN":
                for i in creatures:
                    if i.x == newPlayer.x and i.y == newPlayer.y + 1:
                        i.interact(newPlayer)
                for i in treasures:
                    if i.x == newPlayer.x and i.y == newPlayer.y + 1:
                        i.tryOpen()
                        i.update()
                        i.giveItem(newPlayer)
                        
        
        else: 
            pass



update()

#def (target, posx, posy)



