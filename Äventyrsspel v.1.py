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
        for i, item in enumerate(self.inventory, 1):
            print(i, '. ' + item, end='', sep= '\n' )
        

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
                self.hp = 200
                print(f'''
    Du dog
    Liv kvar: [{self.lives}]
    200 hp återställs...
            ''')
                sleep(1)
            

        
    def room_trap(self):
        print("Oh no! It's a trap")
        trap_damage = rand.randint(10,100)
        self.hp = self.hp - trap_damage
        sleep(1)
        print(f"Du tog {trap_damage} skada")
        sleep(1)

    def room_monster(self):
        monster = 120 + 10*self.lvl
        print("Ett monster har dykt upp!!!")
        print(f"Monstret har {monster} HP")
        sleep(2)
        while True:
            damage = rand.randint(15,100)
            monster = monster - damage
            input("\nTryck <Enter> för att attackera monstret")
            sleep(2)
            print(f"\nMonstret tog {damage} damage")
            print(f"Monstret har {monster} HP kvar")
            sleep(2)
            if monster <= 0:
                print("\nDu besegrade monstret!")
                sleep(1)
                self.lvl = self.lvl +1
                print("Du gick upp i LVL!")
                sleep(1)
                print(f"Du är nu LVL{self.lvl}!")
                sleep(2)
                break
            damage1 = rand.randint(15,200)
            self.hp = self.hp - damage1
            sleep(1)
            print(f"\nDu tog {damage1} damage")
            print(f"Du har {self.hp} Hp kvar")
            sleep(1)
            if self.hp <= 0:
                print("Du dog")
                sleep(1)
                Player1.losing_lives
                if Player1.lives == 0:
                    break

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

    def add_items_in_inventory(self):
        if len(items_in_inventory) < 5:
            choice_item = input(f'''
[1] Om du vill kasta bort föremålet [2] Om du vill spara föremålet 
--->''')
            if choice_item == '1':
                print("Du kastade bort föremålet")
            elif choice_item == '2':
                print(f"Du la till {item_in_chest} i ditt inventory")
                items_in_inventory.append(item_and_effekt)
        
        if len(items_in_inventory) >= 5:
            choice_item = input('''
Ditt inventory ar fullt
[1] Om du vill kasta bort föremålet [2] Om du vill byta ut något av de items som du redan har
--->
            ''')
            if choice_item == '1':
                print("Du kastade bort föremålet")
            
            if choice_item == '2':
                Player1.show_inventory()
                item_number_switch = int(input('''
Vilket nummer har det foremol som du vill ta bort?
Ga tillbaka [G]
--->
                ''')).lower()
                if item_number_switch == 'g':
                    pass
                else:
                    if_sure = input('''
Ar du saker pa att du vill byta ut detta item?
[Ja] = 1
[Nej] = 2
                    ''')
                    if if_sure == '1':
                        items_in_inventory.append(item_number_switch - 1)
                        items_in_inventory.append(item_and_effekt)


#Items i spelarens inventory
items_in_inventory = []

#Item kategories
list_kategories = ['Sword', 'Potion', 'Ring']  

#Diffrent items
list_swords = ["Woodensword", "Lightsaber"]
list_rings =  ['Force ring', 'Ring of fire']
list_potion = ['Health potion', 'Strength potion']

#Swords strength
swords_strength = {
    "Woodensword": 2,
    "Lightsaber": 1000,
}

#Potion Effekt
potion_effekt = {
    "Health potion": 50,
    "Strength potion": 50,
}

#Ring strength
ring_strength = {
    "Force ring": 50,
    "Ring of fire": 50,
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
    string = '''
    Du öppnar dina ögon, det är totalt mörker och du kan endast urskilja
    några fåtal konturer. Marken under dig är kall som is. 
        "Vad är detta för ställe?", tänker du för dig själv.
        "Drömmer jag fortfarande?"
    Längst bort bland rummets outforskade partier skymms en ljuskälla av
    allt mörker. Ljuset växer starkare och starkare; efter en kort stund
    blir det tillräckligt ljust för att kunna skymta en siluett.
        "Är jag trots allt inte ensam här nere?"
        "Hallå? Vem är där?", lyckas du få ut med ett föträngt utrop.
        "Mitt namn är laban, du hör inte hemma här", säger den okända
    rösten som tycks tillhöra en pojke i tonåren.
        "Hur hamnade jag här?", säger du.
        "Under flertal decennier har människor som du, dykt upp i våran
    värld under okända omständigheter. Till skillnad från mitt folk kan
    ni människor inte stanna här länge, om ni inte önskar att stanna här
    för evigt förstås. Du ser... Jag var också en människa som du en gång
    i tiden. Men som du kan se var jag för långsam och nu kvarstår endast
    en skepnad av mitt sanna jag."
        "Hur tar jag mig härifrån?", frågar du oroligt.
        "Det finns endast ett sätt att ta sig härifrån, bakom dessa tre
    dörrar finner du antingen en kista med ett föremål som kan hjälpa dig
    under din resa, en fiende som kommer göra allt i sin makt för att döda
    dig och slutligen finns det fällor, dessa vill du undvika, ingen har 
    någonsin lämnat ett rum med en fälla oskadd. Nu måste du ge dig iväg,
    tiden är viktig här. Just det, jag glömde fråga dig en sak"
    

    '''
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.03)
    sleep(1)
    
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
                pass
            elif chosen_number == '2':
                Player1.show_inventory()
            elif chosen_number == '3':
                break
            elif chosen_number == '4':
                end = input("Är du säker på att du vill avsluta? [Ja]: ")
                end = end.lower()
                if end == "ja":
                    return True

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
  
def new_item_information(item_in_chest):
    if item_in_chest in list_swords:
        print(f"hittade {item_in_chest} med STR:{swords_strength[item_in_chest]} i kistan")
        item_and_effekt = (f"{item_in_chest} --- STR:{swords_strength[item_in_chest]}")
        return item_and_effekt

    elif item_in_chest in list_rings:
        print(f"Du hittade {item_in_chest} med STR:{ring_strength[item_in_chest]}")
        item_and_effekt = (f"{item_in_chest} --- STR:{ring_strength[item_in_chest]}")
        return item_and_effekt
                
    elif item_in_chest in list_potion:
        print(f"Du hittade {item_in_chest} med Effekt:{potion_effekt[item_in_chest]}")
        item_and_effekt = (f"{item_in_chest} --- Effekt:{potion_effekt[item_in_chest]}")
        return item_and_effekt
  
    


def boss_monster():
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
    


#Main Program
#           Namn Strength HP  LVL Lives Inventory
Player1 = Player('x', 10, 200, 0, None, items_in_inventory)

start_game()
Player1.difficulty()


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
        end_game = meny()
        if end_game == True:
            print("programmet avslutas")
            break        
    
    elif given_input == 'v' or given_input == 'm' or given_input == 'h':
        room_type = door_chance()
        if room_type == 1:
            item_in_chest = room_chest()
            item_and_effekt = new_item_information(item_in_chest)
            Player1_Item.add_items_in_inventory()
            input("\nTryck <Enter> för att fortsätta")
        elif room_type == 2:
            Player1.room_monster()
        elif room_type == 3:
            Player1.room_trap()
            Player1.losing_lives()
            if Player1.lives == 0:
                end_game = True
                print("LIVES LEFT: [0]")
                print("GAME OVER!")
                break




if end_game == False:
    boss_monster()
    while True:
        pass
