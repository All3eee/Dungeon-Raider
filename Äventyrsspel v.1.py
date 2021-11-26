#Använd sleep() istället för time.sleep()
#Man kan berätta i början hur man öppnar inventory etc.
from Functions import animation
import random as rand
import sys
from time import sleep

class Player():
    def __init__(self, name, strength, hp, lvl, lives, inventory):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.lives = lives
        self.inventory = inventory

    def inventory():
        pass
    
    def abilites(self):
        print(f'''
        Strength: {self.strength}
        Level: {self.lvl}
        Lives: {self.lives}
        
        ''')
    
    def difficulty(self):
        print("Du kommer nu att få bestämma förinställningar")
        while True:
            difficulty = input('''
                Svårighetsgrad
        Normal[1]           Hardcore[2]
        ---> ''')
            if difficulty == '1':
                self.lives = 3
                break
            elif difficulty == '2':
                self.lives = 1
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
    def __init__(self, type_of_item, strength_bonus):
        self.type_of_item = type_of_item
        self.strength_bonus = strength_bonus
    
    def item_type_decider():
        type = rand.randint(1, 100)
        if type == (1, 40):
            type_of_item = "sword"
        elif type == (41, 60):
            type_of_item = "ring"
        elif type == (61, 100):
            type_of_item = "potion"

    def item_type_sword():
        rarity = rand.randint(1, 100)
        if rarity == (1, 50):
            return(wooden_sword)
        if rarity == (51, 100):
            return(laser_saber)



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
        chosen_input = input("Ange här --> ")
        chosen_input = chosen_input.lower()
        if chosen_input == 'v' or 'm' or 'h' or 'e':
            return chosen_input

def door_chance():
    pass

def room_chest():
    pass
    
def room_trap():
    print("Oh no! It's a trap")
    
def room_monster():
    pass

def boss_monster():
    pass        

#Main Program
Player1 = Player('x',10,200,0, 3, [])
animation()

start_game()
Player1.difficulty()

Prolog()

Player1.set_character()

while True:
    if Player1[0] == 10:
        break
    given_input = the_room()
    if given_input == 'e':
        while True:
            chosen_number = meny()
            if chosen_number == '1':
                abilities():
            elif chosen number == '2':
                Player1.inventory():
    elif given_input == 'v':
        print("Vänster dörr öppnas")
        room_type = door_chance()
        if room_type == 1:
            room_chest()
        elif room_type == 2:
            room_monster()
        elif room_type == 3:
            room_trap()
    elif given_input == 'm':
        print("Dörren i mitten öppnas")
    elif given_input == 'h':
        print("Höger dörr öppnas")

boss_monster()
while True:
    pass