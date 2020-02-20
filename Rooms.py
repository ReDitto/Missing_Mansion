import time
from Things import *


class room:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def introtext (self):
        raise NotImplementedError()

    def modplayer (self, player):
        raise NotImplementedError()

class nursery(room):
    def nurserytext (self):
        time.sleep(2)
        print("\nEyeing the room, you notice three things that stand out quite a bit from the rest of the room:")
        time.sleep(2.5)
        print("\t- An oddly shaped lamp")
        time.sleep(1.75)
        print("\t- A small bookshelf with only two books")
        time.sleep(1.75)
        print("\t- And a myriad of different colored socks scattered across the floor.")
    def modplayer (self, player):
        pass

class loft(room):
    def lofttext (self):
        print("")#placeholder
    def modplayer (self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("placeholder something about the undefinable ghost attacking you".format(self.enemy.damage, player.hp))