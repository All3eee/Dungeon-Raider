import random as rand
import sys
import time

def meny():
    string ='''
-----------------------------
Välkommen till Dungeon Raider
-----------------------------'''
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)

class Player():
    def __init__(self, name, strenght, hp, lvl):
        self.name = name
        self.strenght = strenght
        self.hp = hp
        self.lvl = lvl

class Item():
    def __init(self, strenght_bonus):
        self.strenght_bonus = strenght_bonus


#Huvudprogram

while True:
    meny()
    break