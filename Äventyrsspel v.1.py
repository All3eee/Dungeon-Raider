import random as rand
import sys
from time import sleep
from Animationer import *
from Hänga_Gubbe import *


end_game = False #Variabel som används för att stänga av spelet helt
player_inventory = [] #Spelarens inventory

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
        Namn
        Styrka: {self.strength}
        HP: {self.hp}
        MAX HP: {self.max_hp}
        Level: {self.lvl}
        Liv: {self.lives}
        ''')
        input("\nTryck <Enter> för att stänga sidan")

    def difficulty(self):
        print("Vad vill du ha för svårighetsgrad?")
        while True:
            difficulty = input('''
    
    Normal[1]        
    Hardcore[2]
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
        print("\nLaban: Vad heter du?")
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
        potion_value_list = [] #Lista för potions i inventoryt
        potion_position_in_inventory = []  #Används för att veta platserna för de olika potions
        number_of_potion = 1 #Används för rangordning
        number_in_inventory = 0 #Används för att veta var potions är i inventory
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
            if potion_choice <= len(potion_value_list) and potion_choice < 0:
                health_increase = potion_value_list[potion_choice- 1]
                self.hp = self.hp + health_increase
                            
                position = potion_position_in_inventory[potion_choice-1]
                player_inventory.pop(position) #Tar bort potion från inventory
            else:
                print("Det du angav existerar ej")
                sleep(1)
            
                        

                    

    def room_trap(self):
        sleep(1)
        print("\nOh no! It's a trap")
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
                        print(f"{number}.{i.name}  ---  {i.strength} STR", sep =' ')
                        sword_list.append(i.strength)
                        number += 1

                if number == 1:
                    print("Du har inget vapen och måste slåss med händerna!")
                    return self.strength + rand.randint(-10,20)
                else:     
                    while True:
                        weapon_choice = input("Vilket nummer har vapnet som du vill använda? --> ")
                        number_or_not = weapon_choice.isdigit()
                        if number_or_not == True:
                            weapon_choice = int(weapon_choice)
                            if weapon_choice > 0 and weapon_choice <= len(sword_list):
                                random_damage = rand.randint(1,10) - rand.randint(1,10)
                                damage_of_weapon = sword_list[weapon_choice - 1] + self.strength + random_damage
                                return damage_of_weapon
                            else:
                                print("Det du angav existerar ej")
                        else:
                            print("Det du angav existerar ej")
            if menu_choice == "69":
                return 1000000

            elif menu_choice == "2":
                Player1.use_potion()
                    
            elif menu_choice == "3":
                Player1.abilities()
                continue

    
    def room_monster(self):
        
        if self.lvl >= 10:
            laban()
            monster_hp = 500
            monster_namn = 'Laban'
        else: 
            monster_namn = monster_animation()
            monster_hp = 120 + 10*self.lvl
            
        print(f"{monster_namn} har {monster_hp} HP")
        sleep(1)
        while True:
            damage = Player1.battle_menu()

            input(f"\nTryck <Enter> för att attackera {monster_namn}")
            sleep(1)
            monster_hp = monster_hp - damage
            print(f"\n{monster_namn} tog {damage} damage")
            if monster_hp <= 0:
                monster_hp = 0
            print(f"{monster_namn} har {monster_hp} HP kvar")
            sleep(2)
            if monster_hp <= 0:
                if self.lvl >= 10:
                    break
                print(f"\nDu besegrade {monster_namn}!")
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
                    return 'dead'

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
        self.strength += rand.randint(1,20)
        if self.category == 'Potion':
            if self.attribute == 'Health': #Health potions
                print(f"Som ger dig +{self.strength} HP när du dricker den")
            elif self.attribute == 'STR': #Strength potions
                print(f"Som ger dig +{self.strength} extra styrka")
        
        elif self.category == 'Ring':
            if self.attribute == 'STR': #Strength Rings
                print(f"Som ger dig +{self.strength} styrka")
            elif self.attribute == 'Health': #Health Ring
                print(f"Som ger dig +{self.strength} extra på ditt MAX HP")
        
        elif self.category == 'Sword': #Alla svärd
            print(f"Med styrkan: {self.strength}")
        
        while True:
            if len(player_inventory) < 5:
                choice_item = input(f'''
[1] Om du vill kasta bort föremålet 
[2] Om du vill spara föremålet 
---> ''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2':
                    if self.category == 'Ring':
                        if self.attribute == "Health":
                            Player1.max_hp += self.strength
                        elif self.attribute == "STR":
                            Player1.strength += self.strength
                    player_inventory.append(self)
                    break
        
            elif len(player_inventory) >= 5:
                choice_item = input('''
Ditt inventory är fullt
[1] Om du vill kasta bort föremålet 
[2] Om du vill byta ut något av de items som du redan har
---> ''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2':
                    show_inventory()
                    item_number_switch = input(f'''
Vilket nummer har det föremål som du vill ta bort [1], [2], [3], [4], [5]
Tryck på för att gå tillbaka [G]
---> ''').lower()
                    if item_number_switch == 'g':
                        continue
                    else:
                        
                       if_sure = input('''
Är du säker på att du vill byta ut detta item?
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
                        player_inventory.append(self)
                        break
                    if if_sure == '2':
                        continue

    def popping_item(self):
        if self.category == 'Ring':
            if self.attribute == "Health":
                Player1.max_hp -= self.strength
            elif self.attribute == "STR":
                Player1.strength -= self.strength
                        
                  

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

all_items = [item1, item2, item3, item4, item5, item7, item8, item9, item10, item11, item12]
#Item 6 existerar inte just nu.
#Vid tilläg av item, lägg in det också i listan ovanför.


#Random Item + Room chest
def room_chest():
    print("Det är en kista!")

    while True:
        chest_item = rand.randint(1,5) #Slumpar de olika kategorier av föremål
        category_items = [] #En lista för de föremål med kategorin som har slumpats fram
        
        if chest_item == 1: #20% för en ring
            for item in all_items:
                if item.category == 'Ring':
                    category_items.append(item)
        
        elif chest_item == 2 or chest_item == 3: #40% för ett svärd
            for item in all_items:
                if item.category == 'Sword':
                    category_items.append(item)        
        
        elif chest_item == 4 or chest_item == 5: #40% för potion
            for item in all_items:
                if item.category == 'Potion':
                    category_items.append(item) 
        
        amount_in_list = len(category_items)-1 #Antal föremål med kategorin som har slumpats fram
        random_item = rand.randint(0,amount_in_list)
        if category_items[random_item] in player_inventory: #Om föremålet redan finns i inventoryt
            pass 
        else:  #Föremålet finns ej i inventory
            category_items[random_item].add_items_in_inventory()
            break




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
            if i.category == 'Sword':
                print(f"{number}.{i.name}  ---  {i.strength} STR", sep =' ')
            else:
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
    
    while True:
        completion_or_death = hänga_gubbe()         #Från filen Hänga_Gubbe.py
        if completion_or_death == 'dead':
            Player1.hp = 0
            Player1.losing_lives
            if  Player1.lives == 0:
                return 'dead'
            else:
                print("Du förlora ett liv, du får en chans till att köra hänga gubbe")
        else:
            break
    
    print("BOSSS FIGHT PÅ GÅNG")
    sleep(1)
    dead_or_win = Player1.room_monster()
    if dead_or_win == 'dead':
        return dead_or_win
    
    while True:
        print("\nGör slut på Labans liv [1]")
        print("Spara hans liv         [2]")
        life_or_death = input('''
        Vad väljer du?
        ---> ''')

        if life_or_death == '1':
            laban_death()
            dead_laban()
            return 'laban_dead'
        elif life_or_death == '2':
            laban_alive()
            return 'laban_alive'
        else:
            print("Laban: DÖDAA MIG!!!")




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

title() #Från filen "Animationer"
start_game()
Prolog() #Från filen "Animationer"
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
            if Player1.lvl >= 10:
                break
            Player1.room_monster()
            input("\nTryck <Enter> för att fortsätta") 
        elif room_type == 3:
            Player1.room_trap()
            Player1.losing_lives()
            if Player1.lives <= 0:
                end_game = True
                break
    elif given_input == "420":
        room_chest()
        # Player1.room_monster()


if end_game == False:
    dead_or_not = boss_monster()
    if dead_or_not == 'dead':
        end_game = True
    else:
        end_credit()

if end_game == True:
    print("LIVES LEFT: [0]")
    print("GAME OVER!")


    
    

