import random as rand
import sys
from time import sleep
from Animationer import *

#Variabel som används för att stänga av spelet helt
end_game = False
player_inventory = []

class Player():
    def __init__(self, name, strength, hp, max_hp, lvl, lives, inventory):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.max_hp = max_hp
        self.lvl = lvl
        self.lives = lives
        self.inventory = inventory
        

    def abilities(self):
        print(f'''
        Strength: {self.strength}
        HP: {self.hp}
        MAX HP: {self.max_hp}
        Level: {self.lvl}
        Lives: {self.lives}
        
        ''')
        input("\nTryck <Enter> för att stänga sidan")

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
        print("Laban: Vad heter du?")
        self.name = input("Ange ditt namn ->: ")
        print(f'''
Laban: Jasså, så du heter {self.name}.
       Du ser ut att ha varit med om en hel del.
        ''')

    def losing_lives(self):
        if self.hp <= 0:
            self.lives = self.lives -1
            if self.lives != 0:
                self.hp = self.max_hp
                print(f'''
    Du dog
    Liv kvar: [{self.lives}]
    {self.max_hp} hp återställs...
            ''')
                sleep(1)
    
    def use_potion(self):
        potion_value_list = []
                    
        #Används för att veta platserna för de olika potions
        potion_position_in_inventory = []
        number_of_potion = 1
        number_in_inventory = 0
        for i in player_inventory:
            if i.category == 'Potion':
                print(f"{number_of_potion}.{i.name}  ---  +{i.strength} Health", sep =' ')
                potion_value_list.append(i.strength)
                            
                #Lägger till platserna för de olika potions i Player inventory
                potion_position_in_inventory.append(number_in_inventory)
                number_of_potion += 1
            number_in_inventory +=1
        if number_of_potion == 1:
            print("\nDu har inga potions i ditt inventory") 
            
        else:
            potion_choice = int(input("Vilket nummer har den potion som du vill använda? --> "))
            health_increase = potion_value_list[potion_choice- 1]
            self.hp = self.hp + health_increase
                        
            #Tar bort potion från inventory
            position = potion_position_in_inventory[potion_choice-1]
            player_inventory.pop(position)
                    

    def room_trap(self):
        print("Oh no! It's a trap")
        trap_damage = rand.randint(10,80)
        self.hp = self.hp - trap_damage
        sleep(1)
        print(f"Du tog {trap_damage} skada")
        sleep(1)

 

    def battle_menu(self):
        while True:
            menu_choice = input('''
[1] Attackera
[2] Använda potion
[3] Spelare information
---> ''')
            if menu_choice == "1":
                number = 1
                sword_list = []
                for i in player_inventory:
                    if i.category == 'Sword':
                        print(f"{number}.{i.name}  ---  +{i.strength} STR", sep =' ')
                        sword_list.append(i.strength)
                        number += 1

                if number == 1:
                    print("Du har inget vapen och måste slåss med händerna!")
                    return self.strength + rand.randint(-10,20)
                else:     
                    weapon_choice = int(input("Vilket nummer har vapnet som du vill använda? --> "))
                    random_damage = rand.randint(1,20) - rand.randint(1,20)
                    damage_of_weapon = sword_list[weapon_choice - 1] + self.strength + random_damage
                    return damage_of_weapon
            if menu_choice == "69":
                return 1000000

            elif menu_choice == "2":
                Player1.use_potion()
                    
            elif menu_choice == "3":
                Player1.abilities()
                continue

    
    def room_monster(self):
        monster = 120 + 10*self.lvl
        monster_animation()
        print(f"Monstret har {monster} HP")
        sleep(1)
        while True:
            damage = Player1.battle_menu()

            input("\nTryck <Enter> för att attackera monstret")
            sleep(1)
            monster = monster - damage
            print(f"\nMonstret tog {damage} damage")
            if monster <= 0:
                monster = 0
            print(f"Monstret har {monster} HP kvar")
            sleep(2)
            if monster <= 0:
                print("\nDu besegrade monstret!")
                sleep(1)
                self.lvl = self.lvl +1
                print("Du gick upp i LVL!")
                sleep(1)
                print(f"Du är nu LVL {self.lvl}!")
                sleep(2)
                break
            damage1 = rand.randint(2*self.lvl,20 + 25*self.lvl)
            self.hp = self.hp - damage1
            sleep(1)
            print(f"\nDu tog {damage1} damage")
            if self.hp <= 0:
                self.hp = 0
            print(f"Du har {self.hp} Hp kvar")
            sleep(1)
            if self.hp <= 0:
                Player1.losing_lives()
                if Player1.lives == 0:
                    break

class Item():
    def __init__(self, category, name, strength, attribute):
        self.category = category
        self.name = name
        self.strength = strength
        self.attribute = attribute
        
    def get_strength(self):
        return self.strength

    def add_items_in_inventory(self):
        print(f"\nDu har fått {self.name}")
        
        if self.category == 'Potion':
            #Health potions
            if self.attribute == 'Health':
                print(f"Som ger dig +{self.strength} HP när du dricker den")
            #Strength potions
            elif self.attribute == 'STR':
                print(f"Som ger dig +{self.strength} extra styrka")
        
        elif self.category == 'Ring':
            #Strength Rings
            if self.attribute == 'STR':
                print(f"Som ger dig +{self.strength} styrka")
            #Health Ring
            elif self.attribute == 'Health':
                print(f"Som ger dig +{self.strength} extra på ditt MAX HP")
        
        #Alla svärd
        elif self.category == 'Sword':
            print(f"Med styrkan: {self.strength}")
        
        while True:
            if len(player_inventory) < 5:
                choice_item = input(f'''
[1] Om du vill kasta bort föremålet [2] Om du vill spara föremålet 
--->''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2':
                    if self.category == 'Ring':
                        if self.attribute == "Health":
                            Player1.max_hp += self.strength
                        elif self.attribute == "STR":
                            Player1.strength += self.strength
                    return self
        
            elif len(player_inventory) >= 5:
                choice_item = input('''
Ditt inventory är fullt
[1] Om du vill kasta bort föremålet [2] Om du vill byta ut något av de items som du redan har
---> ''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2':
                    show_inventory()
                    item_number_switch = input('''
Vilket nummer har det föremål som du vill ta bort?
Gå tillbaka [G]
---> ''').lower()
                    if item_number_switch == 'g':
                        continue
                    else:
                        
                       if_sure = input('''
Ar du saker pa att du vill byta ut detta item?
[Ja] = 1
[Nej] = 2
--->''')
                    if if_sure == '1':
                        item_number_switch = int(item_number_switch)
                        player_inventory[item_number_switch-1].popping_item()
                        player_inventory.pop(item_number_switch-1)
                        if self.category == 'Ring':
                            if self.attribute == "Health":
                                Player1.max_hp += self.strength
                            elif self.attribute == "STR":
                                Player1.strength += self.strength
                        return self
                    if if_sure == '2':
                        continue

    def popping_item(self):
        if self.category == 'Ring':
            if self.attribute == "Health":
                Player1.max_hp -= self.strength
            elif self.attribute == "STR":
                Player1.strength -= self.strength
                        
                  

#Items i spelarens inventory

# Category, Name, Strength/health
item1 = Item("Sword", "Stick", 10, "STR")
item2 = Item("Sword", "Lightsaber", 200, "STR")
item9 = Item("Sword", "Stone Sword", 40, "STR")
item10 = Item("Sword", "Gold Sword", 60, "STR")
item11 = Item("Sword", "Diamond", 70, "STR")
item12 = Item("Sword", "Machine gun", 300, "STR")
item3 = Item("Ring", "Force Ring", 50, "STR")
item4 = Item("Ring", "Ring of fire", 50, "STR")
item5 = Item("Potion", "Health Potion", 50, "Health")
item7 = Item("Ring", "Health Ring", 50, "Health")
item8 = Item("Potion", "Borogor", 100, "Health")


def room_chest():
    print("Det är en kista!")

    chest_item = rand.randint(1, 200)
    if chest_item > 0 and chest_item <= 21:
        appending_item = item1.add_items_in_inventory()
    elif chest_item > 21 and chest_item <= 26:
        appending_item = item2.add_items_in_inventory()
    elif chest_item > 26 and chest_item <= 38:
        appending_item = item3.add_items_in_inventory()
    elif chest_item > 38 and chest_item <= 61:
        appending_item = item4.add_items_in_inventory()
    elif chest_item > 51 and chest_item <=76:
        appending_item = item5.add_items_in_inventory()
    elif chest_item > 76 and chest_item <= 100 :
        appending_item = item12.add_items_in_inventory()
    elif chest_item > 100 and chest_item <=120 :
        appending_item = item7.add_items_in_inventory()
    elif chest_item > 120 and chest_item <=140:
        appending_item = item8.add_items_in_inventory()
    elif chest_item > 140 and chest_item <=160 :
        appending_item = item9.add_items_in_inventory()
    elif chest_item > 160 and chest_item <=180 :
        appending_item = item10.add_items_in_inventory()
    elif chest_item > 180 and chest_item <=200 :
        appending_item = item11.add_items_in_inventory()
    
    player_inventory.append(appending_item)

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
    while True:
        print('''\n
    Ange [1] för egenskaper
    Ange [2] för inventory
    Ange [3] för att stänga meny
    Ange [4] för att avsluta spel
    ''')
        chosen_number = input("---> ")
        if chosen_number == '1' or '2' or '3' or '4':
            if chosen_number == '1':
                Player1.abilities()
            elif chosen_number == '2':
                inventory_usage()
            elif chosen_number == '3':
                break
            elif chosen_number == '4':
                end = input("Är du säker på att du vill avsluta? [Ja]: ")
                end = end.lower()
                if end == "ja":
                    print("programmet avslutas")
                    sleep(0.5)
                    print("3")
                    sleep(0.5)
                    print("2")
                    sleep(0.5)
                    print("1")
                    return True

def show_inventory():
    number = 1
    for i in player_inventory:
        if i == None:
            break
        if i.attribute == 'STR':
            print(f"{number}.{i.name}  ---  +{i.strength} STR", sep =' ')
        elif i.attribute == 'Health':
            print(f"{number}.{i.name}  ---  +{i.strength} Health", sep =' ')
        number += 1

def inventory_usage():
    while True:
        if len(player_inventory) > 0:
            pass
        else:    
            print("Det är tomt i ditt inventory")
            input("\nTryck <Enter> för att fortsätta")
            break
        show_inventory()
        choice_input = input('''
    Tryck på [1] för att ta bort föremål
    Tryck på [2] för att använda potion
    Tryck på [3] för att återvända till meny
        ''')
        if choice_input == '1':
            item_number_switch = input('''
    Vilket nummer har det föremål som du vill ta bort?
    Gå tillbaka [G]
    ---> ''').lower()
            if item_number_switch == 'g':
                continue
            else:
                if_sure = input('''
    Ar du saker pa att du vill byta ut detta item?
    [Ja] = 1
    [Nej] = 2
    --->''')
            if if_sure == '1':
                item_number_switch = int(item_number_switch)
                player_inventory[item_number_switch-1].popping_item()
                player_inventory.pop(item_number_switch-1)
        elif choice_input == '2':
            Player1.use_potion()               
        elif choice_input == '3':
            break


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
        if chosen_input == "420":
            return chosen_input

def door_chance():
    door_type = rand.randint(1,3)
    return door_type


def boss_monster():
    laban()
    pass

   

def animation_door():
    print(f'''
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
                
                ------------------------
                |        LIV:{Player1.lives}         |
                |        HP: {Player1.hp}       |
                ------------------------
    ''')
    print('''
    Vänster dörr [V], Mitten dörr [M], Höger dörr [H]    
    Meny [E]  
        ''')
    



#             Namn Strength HP MAX_HP LVL Lives Inventory
Player1 = Player('x', 20, 200, 200, 0, None, player_inventory)

#Main Program
title()
start_game()
Player1.difficulty()


Player1.set_character()

while True:
    
    animation_door()

    given_input = the_room()

    if given_input == 'e':
        end_game = meny()
        if end_game == True:
            break        
    
    elif given_input == 'v' or given_input == 'm' or given_input == 'h':
        room_type = door_chance()
        if room_type == 1:
            room_chest()
            input("\nTryck <Enter> för att fortsätta")
        elif room_type == 2:
            Player1.room_monster()
            input("\nTryck <Enter> för att fortsätta") 
        elif room_type == 3:
            Player1.room_trap()
            Player1.losing_lives()
            if Player1.lives <= 0:
                end_game = True
                print("LIVES LEFT: [0]")
                print("GAME OVER!")
                break
    elif given_input == "420":
        room_chest()


if end_game == False:
    boss_monster()
    while True:
        pass


