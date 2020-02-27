import time
import os
from Actions import *
from Bag import *
from Rooms import *
from Things import *

print("\n\t\t  THE MISSING MANSION")
time.sleep(1.5)
playername = input("\n\n\n\n\t\tENTER YOUR NAME TO BEGIN\n\n\t")

if playername != "Zorc" and playername != "zorc" and playername != "Zork" and playername != "zork": #This part is a Zork easter egg
    time.sleep(0.75)
    print("\tExcellent... One moment please.\n\t(I recommend maximizing the window)")
elif playername == "Zorc" or playername == "zorc" or playername == "Zork" or playername == "zork":
    time.sleep(0.75)
    print("\t...")
    time.sleep(1.75)
    print("\tYou think you're funny, huh?")
    time.sleep(1.75)
    print("\tYeah, yeah, yeah... I'll start the game now. *ahem*")

intro = True

while(intro):
    time.sleep(5)
    os.system('cls')
    time.sleep(1.75)
    print("\nYou wake up from your long and dazed trance. You're not sure how long you've been out cold. After taking a second to grasp your envoirnment, you look around to see where you were.")
    time.sleep(2.75)
    print("After a breif observation of your surroundings, the room looks all too familiar. After a moment of thought, it's clear that you've finally found it: The Missing Quinelly Mansion.")
    time.sleep(2.75)
    print("You have somehow ended up in the nurserey. On the bright side, months and almost years of research and investigation have finally paid off. It has been found at last!")
    time.sleep(2.75)
    print("Unfortunatley, you're only present with the clothes on your back, and without proper equipment to record findings of any sort.")
    time.sleep(2.75)
    print("You must get out as quickly as possible so you may return to do proper research, lest your name be added to the disappearances the home is infamous for.")
    break

intro = False

nurser = nursery (x = 2, y = 5)
nurser.nurserytext()

innursery = True
while (innursery):
    time.sleep(0.75)
    command = input("\nWhat will you do?\n\t")
    if command == "look lamp" or command == "look oddlamp" or command == "lootat lamp" or command == "lookat oddlamp" or command == "look at lamp" or command == "look at oddlamp" or command == "go lamp" or command == "go oddlamp" or command == "goto lamp" or command == "goto oddlamp" or command == "go to lamp" or command == "go to oddlamp" or command == "check lamp" or command == "check oddlamp":
        time.sleep(0.75)
        print("You walk to the lamp and puzzle at it for a bit. You've come to the conclusion that, although it isn't ideal to carry around everywhere, it could be very resourceful.")
        time.sleep(1.75)
        print("\t*You take the odd lamp.*")
        time.sleep(0.75)
        #placeholder - player.inventory append(self.oddlamp)
    elif command == action:
        print(action)
    elif command != action:
        time.sleep(0.75)
        print("\nThat isn't a valid command.")

innursery = False

lof = loft (x = 2, y = 3 & 4)
lof.lofttext()

inloft = True
while (inloft):
    time.sleep(0.75)
    command = input("\nWhat will you do?\n\t")
    #if command ==