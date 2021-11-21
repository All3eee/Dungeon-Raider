#Använd sleep() istället för time.sleep()
#Man kan berätta i början hur man öppnar inventory etc.

import random as rand
import sys
from time import sleep

class Player():
    def __init__(self, name, strength, hp, lvl, respawn, inventory):
        self.name = name
        self.strength = strength
        self.hp = hp
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

    def set_character(self):
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

def Prolog():
    print('''
    Det var en gång för länge sedan
    Laban berättar om sitt liv blah blah blah 
    ''')
    sleep(1)

def meny():
    while True:
        print('''
    Ange [1] för egenskaper
    Ange [2] för inventory
    Ange [3] för att stänga meny
    Ange [4] för att avsluta spel
    ''')
        chosen_number = input("---> ")
        if chosen_number == '1' or '2' or '3' or '4':
            return chosen_number
    

def the_room():
    while True:
        print('''
 ____________   ____________   ____________
|            | |            | |            |
|            | |            | |            |
|            | |            | |            |
|      V     | |      M     | |      H     | 
|            | |            | |            |
|            | |            | |            |
|____________| |____________| |____________|
    
Vänster dörr [V], Mitten dörr [M], Höger dörr [H]    
Meny [E]  
        ''')
        chosen_input = input("Ange här --> ")
        chosen_input = chosen_input.lower()
        if chosen_input == 'v' or 'm' or 'h' or 'e':
            return chosen_input

def door_chance():
    pass

#ska denna vara som en metod i klassen Person?
def inventory():
    pass

def egenskaper():
    pass
        

#Huvudprogram

Player1 = Player('x',10,200,0, True, [])


start_game()
Player1.difficulty()

Prolog()

Player1.set_character()

while True:
    given_input = the_room()
    if given_input == 'e':
        meny()
    elif given_input == 'v':
        print("Vänster dörr öppnas")
    elif given_input == 'm':
        print("Dörren i mitten öppnas")
    elif given_input == 'h':
        print("Höger dörr öppnas")
    break
