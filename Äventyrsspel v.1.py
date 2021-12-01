#Använd sleep() istället för time.sleep()

import random as rand
import sys
from time import sleep

#Variabel som används för att stänga av spelet helt
end_game = False


class Player():
    def __init__(self, name, strength, hp, lvl, lives, inventory):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.lives = lives
        self.inventory = inventory
        
    def show_inventory(self):
        for number, letter in enumerate(self.inventory):
            print("Item:")
            print(*number, letter , sep = "\n")

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

    def losing_lives(self):
        if self.hp <= 0:
            self.lives = self.lives -1
            if self.lives == 0:
                return True
            self.hp = 200
            print(f'''
    Du dog
    Liv kvar: [{self.lives}]
    200 hp återställs...
            ''')

        
    def room_trap(self):
        print("Oh no! It's a trap")
        trap_damage = rand.randint(10,200)
        self.hp = self.hp - trap_damage
        sleep(1)
        print(f"Du tog {trap_damage} skada")
        sleep(1)


    
#Items i spelarens inventory
items_in_inventory = []


class Item():
    def __init__(self, kategories, sword_items, ring_items, potion_items):
        self.kategories = kategories
        self.sword_items = sword_items
        self.ring_items = ring_items
        self.potion_items = potion_items
        
    def item_type_decider(self):
        item_type = rand.choices(self.kategories, weights=(40, 20, 40), k=1 )
        return item_type

    def item_kategory_sword(self):
        item_sword = rand.choices(self.sword_items, weights=(50, 50), k=1)
        return item_sword

    def item_kategory_ring(self):
        item_ring = rand.choices(self.ring_items, weights=(50, 50), k=1)
        return item_ring
    
    def item_kategory_potion(self):
        item_potion = rand.choices(self.potion_items, weights=(50, 50), k=1)
        return item_potion

    def add_items_in_inventory(self,):
        if len(items_in_inventory) < 5:
            print("[1] Om du vill kasta bort föremålet [2] Om du vill spara föremålet")
            choice_item = input("--->")
            if choice_item == '1':
                print("Du kastade bort föremålet")
            elif choice_item == '2':
                print(f"Du la till {item_in_chest} i ditt inventory")
                items_in_inventory.append(item_and_strenght)

#Item kategories
list_kategories = ['Sword', 'Potion', 'Ring']  

#Diffrent items
list_swords = ["Woodensword", "Lightsaber"]
list_rings =  ['Force ring', 'Ring of fire']
list_potion = ['Health potion', 'Strenght potion']

#Swords strength
swords_strenght = {
    "Woodensword": 2,
    "Lightsaber": 1000,
}


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
        if chosen_input == 'v':
            print("Vänster dörr öppnas")
        elif chosen_input == 'v':
            print("Dörren i mitten öppnas")
        elif chosen_input == 'h':
            print("Höger dörr öppnas")
        if chosen_input == 'v' or 'm' or 'h' or 'e':
            return chosen_input

def door_chance():
    door_type = rand.randint(1,3)
    return door_type

def room_chest():
    new_item_kategory = Player1_Item.item_type_decider()
    v = new_item_kategory.pop()
    
    if v == "Sword":
        new_sword_item = Player1_Item.item_kategory_sword()
        return new_sword_item.pop()

    elif v == "Ring":
        new_ring_item = Player1_Item.item_kategory_ring()
        return new_ring_item.pop()

    elif v == "Potion":
        new_potion_item = Player1_Item.item_kategory_potion()
        return new_potion_item.pop()
    
    
def room_monster():
    pass

def boss_monster():
    pass        

def animation_door():
    print('''
      ,-' ;'! `-.         ,-' ;'! `-.         ,-' ;'! `-.
     / :  ! :  . \       / :  ! :  . \       / :  ! :  . :
    |_ ;    :  ;  |     |_ ;    :  ;  |     |_ ;    :  ;  |
    (| .  : (  !  |     (| .  : (  !  |     (| .  : (  !  | 
    |"    [V]    "|     |"    [M]    "|     |"    [H]    "|
    |  :  ; ' (_) l     |  :  ; ' (_) l     |  :  ; ' (_) l
    |  :    .     |     |  :    .     |     |  :    .     |
    || .  . :  :  |     || .  . :  :  |     || .  . :  :  |
    |" ,  | .  .  |     |" ,  | .  .  |     |" ,  | .  .  |
    |__-__;---.___|     |__-__;---.___|     |__-__;---.___|
    
    ''')
    print('''
    Vänster dörr [V], Mitten dörr [M], Höger dörr [H]    
    Meny [E]  
        ''')
    



#Main Program
#           Namn Strength HP  LVL Lives Inventory
Player1 = Player('x', 10, 200, 0, 3, items_in_inventory)

start_game()
Player1.difficulty()

Prolog()

Player1.set_character()

Player1_Item = Item(list_kategories, list_swords, list_rings, list_potion)

Player1.show_inventory()

while True:
    
    animation_door()
    
    '''
    if Player1(3) == 10:
        pass
    '''
    given_input = the_room()

    if given_input == 'e':
        #Det går att göra menyn under till en hel funktion
        while True:
            chosen_number = meny()
            if chosen_number == '1':
                pass
            elif chosen_number == '2':
                Player1.show_inventory()
            elif chosen_number == '3':
                break
            elif chosen_number == '4':
                end = input("Är du säker på att du vill avsluta? [Ja]: ")
                end = end.lower()
                if end == "ja":
                    end_game = True
                    break
                    
        if end_game == True:
            print("programmet avslutas")
            break        
    
    elif given_input == 'v' or given_input == 'm' or given_input == 'h':
        room_type = door_chance()
        if room_type == 1:
            item_in_chest = room_chest()
            if item_in_chest in list_swords:
                print(f"Du hittade {item_in_chest} med STR:{swords_strenght[item_in_chest]} i kistan")
                item_and_strenght = (f"{item_in_chest} --- STR:{swords_strenght[item_in_chest]}")
                Player1_Item.add_items_in_inventory()
                input("\nTryck <Enter> för att fortsätta")
            elif item_in_chest in list_rings:
                print("hej")
            elif item_in_chest in list_potion:
                print("he")
            sleep(2)
        elif room_type == 2:
            room_monster()
        elif room_type == 3:
            Player1.room_trap()
            Player1.losing_lives()
            if Player1.lives == True:
                end_game = True
                print("LIVES LEFT: [0]")
                print("GAME OVER!")
                break




if end_game == False:
    boss_monster()
    while True:
        pass
