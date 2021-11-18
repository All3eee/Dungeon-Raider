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
    def __init__(self, name, strength, hp, lvl):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.lvl = lvl

class Item():
    def __init(self, strength_bonus):
        self.strength_bonus = strength_bonus

def Prolog():
    print("Det var en gång...")
        
#Huvudprogram
while True:
    meny()
    break
