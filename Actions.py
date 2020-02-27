from Bag import *
from Rooms import *

action = {
    "look"
    "lookat"
    "look at"
    "go"
    "goto"
    "go to"
    "check"
    "open"
    "attack"
    "hit"
    "bag": "In your bag, you have:{}",
    "openbag": "In your bag, you have:{}",
    "open bag": "In your bag, you have:{}",
    "checkbag": "In your bag, you have:{}",
    "check bag": "In your bag, you have:{}",
    "inventory": "In your bag, you have:{}"
}

class player():
    def __init__ (self):
        self.inventory = []
        self.hp = 75
        self.location_x, self.location_y, room.nursery
        self.victory = False

    def alive(self):
        return self.hp > 0