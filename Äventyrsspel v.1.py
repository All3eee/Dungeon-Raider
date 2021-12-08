#Använd sleep() istället för time.sleep()

import random as rand
import sys
from time import sleep

#Variabel som används för att stänga av spelet helt
end_game = False
player_inventory = []

class Player():
    def __init__(self, name, strength, hp, lvl, lives, inventory):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.lvl = lvl
        self.lives = lives
        self.inventory = inventory
        
    def show_inventory(self):
        for i in self.inventory:
            print(self.inventory.index(i) +1, end=' ')
            print(" ",i)
        

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
        string = """
        .-----:
       /       |
   __ /   .-.  .|
  /  `\  /   \/  |
  |  _ \/   .==.==.
  | (   \  /____\__:
   \ \      (_()(_()
    \ \            '---._
     \                   \_
  /\ |`       (__)________/
 /  \|     /\___/
|    \     \||VV
|     \     \|_____,
|      \     ______)
\       \  /`
      \(
                """
        print(string)
        print("Ett monster har dykt upp!!!")
        print(f"Monstret har {monster} HP")
        sleep(1)
        while True:
            damage = rand.randint(15,150)
            monster = monster - damage
            input("\nTryck <Enter> för att attackera monstret")
            sleep(1)
            print(f"\nMonstret tog {damage} damage")
            print(f"Monstret har {monster} HP kvar")
            sleep(2)
            if monster <= 0:
                print("\nDu besegrade monstret!")
                sleep(1)
                self.lvl = self.lvl +1
                print("Du gick upp i LVL!")
                sleep(1)
                print(f"Du är nu LVL_{self.lvl}!")
                sleep(2)
                break
            damage1 = rand.randint(10,150)
            self.hp = self.hp - damage1
            sleep(1)
            print(f"\nDu tog {damage1} damage")
            print(f"Du har {self.hp} Hp kvar")
            sleep(1)
            if self.hp <= 0:
                Player1.losing_lives()
                if Player1.lives == 0:
                    break

class Item():
    def __init__(self, category, name, strength, health):
        self.category = category
        self.name = name
        self.strength = strength
        self.health = health
        

    def add_items_in_inventory(self):
        print(f"\nDu har fått {self.name}")
        while True:
            if len(player_inventory) < 5:
                choice_item = input(f'''
[1] Om du vill kasta bort föremålet [2] Om du vill spara föremålet 
--->''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                elif choice_item == '2':
                    return self.name
        
            elif len(player_inventory) >= 5:
                choice_item = input('''
Ditt inventory ar fullt
[1] Om du vill kasta bort föremålet [2] Om du vill byta ut något av de items som du redan har
--->
            ''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
            
                elif choice_item == '2':
                    item_number_switch = int(input('''
Vilket nummer har det föremål som du vill ta bort?
Gå tillbaka [G]
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
                        return self.name

    def get_item_strength(self):
        return self.strength                

#Items i spelarens inventory

#Swords strength
item1 = Item("Sword", "Stick", 10, None)
item2 = Item("Sword", "Lightsaber", 200, None)
item3 = Item("Ring", "Force Ring", 50, None)
item4 = Item("Ring", "Ring of fire", 50, None)
item5 = Item("Potion", "Health Potion", None, 50)
item6 = Item("Potion", "Strength Potion", 50, None)

all_items = [item1, item2, item3, item4, item5, item6]

def room_chest():
        print("Det är en kista!")
        chest_item = rand.randint(1,100)
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
            appending_item = item6.add_items_in_inventory()
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
    tiden är viktig här. Just det, jag glömde fråga dig en sak."
    

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


def boss_monster():
    string = ''' 
    
    '''
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.03)
    sleep(1)
    attack = input("Tryck snabbt på [A] för att attackera Laban!")
    attack = attack.lower()
    if attack == "a":
        
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
Player1 = Player('x', 10, 200, 0, None, player_inventory)

start_game()
Player1.difficulty()


Player1.set_character()


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
            sleep(0.5)
            print("3")
            sleep(0.5)
            print("2")
            sleep(0.5)
            print("1")
            break        
    
    elif given_input == 'v' or given_input == 'm' or given_input == 'h':
        room_type = door_chance()
        if room_type == 1:
            room_chest()
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
