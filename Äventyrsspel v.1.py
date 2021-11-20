#Använd sleep() istället för time.sleep()

import random as rand
import sys
from time import sleep

class Player():
    def __init__(self, name, strength, HP, lvl, respawn, inventory):
        self.name = name
        self.strength = strength
        self.HP = HP
        self.lvl = lvl
        self.respawn = respawn
        self.inventory = inventory
    
    def difficulty(self):
        print("Du kommer nu att få bestämma förinställningar")
        while True:
            respawn_on_off = input('''
        Ska respawn vara på eller av?
        På [1]
        Av [2]
        ---> ''')
            if respawn_on_off == '1':
                self.respawn = True
                break
            elif respawn_on_off == '2':
                self.respawn = False
                break
            else:
                print("\nAnge [1] eller [2]")

    def set_character_name(self):
        print("Laban - Hejsan vem är du?")
        self.name = input("Ange ditt namn: ")
        print(f'''
Laban - Jasså, så du heter {self.name}.
        Du ser ut att ha varit med om en hel del.
        ''')

class Item():
    def __init(self, type_of_item, strength_bonus):
        self.type_of_item = type_of_item
        self.strength_bonus = strength_bonus

def start_game():
    string ='''
-----------------------------
Välkommen till Dungeon Raider
-----------------------------'''
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.03)
    sleep(1)
    input("\nTryck <Enter> för att starta spelet")

def meny():
    pass

def Prolog():
    print('''
    Det var en gång för länge sedan
    Laban berättar om sitt liv blah blah blah 
    ''')
    sleep(1)
        
#Huvudprogram

Player1 = Player('x',10,200,0, True, [])


start_game()
Player1.difficulty()

Prolog()

Player1.set_character_name()

while True:
    meny()
    pass
