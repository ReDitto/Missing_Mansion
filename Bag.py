from Rooms import *
from Actions import *

class player():
    def __init__ (self):
        self.inventory = []
        self.hp = 75
        self.location_x, self.location_y, room.nursery
        self.victory = False

    def alive(self):
        return self.hp > 0

    def printbag(self):
        for item in self.bag:
            print(item, '\n')