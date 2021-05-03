class gameMap():
    def __init__(self, maxwidth, maxheight, mapList):
        self.map = mapList
        self.width = maxwidth
        self.height = maxheight
    
    def createMap(self):
        for i in range(self.height):
            row = []
            for i in range(self.width):
                row.append(' ')
            self.map.append(row)

    def clearOld(self):
        self.map = []
        for i in range(self.height):
            row = []
            for i in range(self.width):
                row.append(' ')
            self.map.append(row)

    def showMap(self):
        for i in self.map:
            print(i)