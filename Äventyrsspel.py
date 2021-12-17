import random as rand
import sys
from time import sleep
from Animationer import *
from Hänga_Gubbe import *


end_game = False #Variabel som används för att stänga av spelet helt
player_inventory = [] #Spelarens inventory

class Player():
    '''
    En klass för att representera spelaren/ personen
    
    ...
    
    Attribut
    --------
    name : str
        namn på spelaren
    strength : int
        styrkan som spelaren har (vapen exkluderat)
    hp : int
        hp som spelaren har
    reset_hp : int
        hp som spelaren får efter att ha dött
    lvl : int
        nivå/level som spelaren är på
    lives : int
        antal liv som spelaren har kvar

    '''
    
    def __init__(self, name, strength, hp, reset_hp, lvl, lives):
        """
        Alla nödvändiga attributer som behövs för spelar objektet

        Parametrar
        ----------
            name : str
                namn på spelaren
            strength : int
                styrkan som spelaren har (vapen exkluderat)
            hp : int
                hp som spelaren har
            reset_hp : int
                hp som spelaren får efter att ha dött
            lvl : int
                nivå/level som spelaren är på
            lives : int
                antal liv som spelaren har kvar
        """
        self.name = name
        self.strength = strength
        self.hp = hp
        self.reset_hp = reset_hp #reset_hp bestämmer hur mycket hp spelaren får efter död.
        self.lvl = lvl
        self.lives = lives

    def get_name(self):
        return self.name
    
    def abilities(self):
        print(f'''
Namn: {self.name}
Styrka: {self.strength}
Level: {self.lvl}
Liv: {self.lives}
HP: {self.hp}''')
        if self.lives != 1:
            print(f'HP efter död: {self.reset_hp}')
        input("\nTryck <Enter> för att stänga sidan")

    def difficulty(self):
        print("\nVad vill du ha för svårighetsgrad?")
        while True:
            difficulty = input('''
Normal[1]        
Hardcore[2]
---> ''')
            if difficulty == '1': #Normal, 3 liv
                self.lives = 3
                break
            elif difficulty == '2': #Hardcore, 1 liv
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
                self.hp = self.reset_hp
                print(f'''
    Du dog
    Liv kvar: [{self.lives}]
    {self.reset_hp} hp återställs...
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
                potion_value_list.append(i.strength) #Lägger in effekten på de olika potions
                            
                #Lägger till platserna för de olika potions i Player inventory
                potion_position_in_inventory.append(number_in_inventory)
                number_of_potion += 1
            
            number_in_inventory +=1
        if number_of_potion == 1:
            print("\nDu har inga potions i ditt inventory")
            
        else:
            potion_choice = input("Vilket nummer har den potion som du vill använda? --> ")
            if potion_choice.isdigit() == True: #Om potion_choice är en siffra
                potion_choice = int(potion_choice) 
                if potion_choice <= len(potion_value_list) and potion_choice > 0: 
                    health_increase = potion_value_list[potion_choice- 1] #Tar ut effekten på den valda potion
                    self.hp = self.hp + health_increase #ökar hp med potionen
                                
                    position = potion_position_in_inventory[potion_choice-1]
                    player_inventory.pop(position) #Tar bort potion från inventory efter användning
                else:
                    print("Det du angav existerar ej")
            else:
                print("Det du angav existerar ej")
                        
 
    def room_trap(self):
        print("\nOh no! It's a trap")
        trap_damage = rand.randint(30,80) #Slumpat damage
        self.hp = self.hp - trap_damage
        sleep(1)
        print(f"Du tog {trap_damage} skada")
        sleep(1)
        Player1.losing_lives() #Om spelaren förlorar liv eller ej

    def battle_menu(self):
        while True:
            menu_choice = input('''
[1] Attackera
[2] Använda potion
[3] Information om spelare
---> ''')
            if menu_choice == "1":
                number = 1 #Används för rangordning
                sword_list_strength = [] #List för de olika svärd i inventory
                sword_list = []
                for i in player_inventory:
                    if i.category == 'Sword': #Om kategorin är ett svärd
                        print(f"{number}.{i.name}  ---  {i.strength} STR --- Durability: {i.durability}", sep =' ') #Skriver ut föremålet
                        sword_list.append(i)
                        sword_list_strength.append(i.strength) #Lägger till föremålets STR i listan
                        number += 1

                if number == 1:
                    print("Du har inget vapen och måste slåss med händerna!")
                    return self.strength + rand.randint(-5,5) #Random extra damage
                else:     
                    while True:
                        weapon_choice = input("Vilket nummer har vapnet som du vill använda? --> ")
                        if weapon_choice.isdigit() == True: #Kollar om inputen är siffror
                            weapon_choice = int(weapon_choice) #Gör om från string till integer
                            if weapon_choice > 0 and weapon_choice <= len(sword_list_strength):
                                
                                #damage_of_weapon är all damage som läggs på, skadan från vapnet, spelarens styrka
                                damage_of_weapon = sword_list_strength[weapon_choice - 1] + self.strength
                                sword_list[weapon_choice - 1].lose_durability(weapon_choice - 1)
                                return damage_of_weapon
                            else:
                                print("Det du angav existerar ej")
                        else:
                            print("Det du angav existerar ej")
            if menu_choice == "69": #Bypass för att döda monstret snabbt
                return 1000000

            elif menu_choice == "2":
                Player1.use_potion() #Använda potion
                    
            elif menu_choice == "3":
                Player1.abilities() #Visar information om spelaren
                continue

    
    def room_monster(self):
        
        if self.lvl >= 10: #Vid level 10 slåss monstret mot laban
            laban()
            monster_hp = 500 #Labans HP är alltid 500 hp
            monster_namn = 'Laban'
        else: 
            monster_namn = monster_animation() #Från filen "Animationer.py"
            monster_hp = 120 + 10*self.lvl #HP på monstret ökar för varje level
            
        print(f"{monster_namn} har {monster_hp} HP")
        sleep(1)
        while True:
            damage_on_monster = Player1.battle_menu()

            input(f"\nTryck <Enter> för att attackera {monster_namn}")
            
            monster_hp = monster_hp - damage_on_monster
            print(f"\n{monster_namn} tog {damage_on_monster} damage")
            if monster_hp <= 0:
                monster_hp = 0
            print(f"{monster_namn} har {monster_hp} HP kvar")
        
            if monster_hp <= 0:
                if self.lvl >= 10:
                    break
                print(f"\nDu besegrade {monster_namn}!")
                sleep(1)
                self.lvl = self.lvl +1
                print("Du gick upp i LVL!")
                sleep(1)
                print(f"Du är nu LVL {self.lvl}!")
                sleep(1)
                break
            
            #Den slumpade skadan från monstret ökar desto högre level spelaren är
            damage1 = rand.randint(2*self.lvl,20 + 25*self.lvl) 
            self.hp = self.hp - damage1 
            sleep(1)
            print(f"\nDu tog {damage1} damage")
            if self.hp <= 0: 
                self.hp = 0 #För att inte visa negativ hp
            print(f"Du har {self.hp} Hp kvar")
            sleep(1)
            if self.hp <= 0: #Om spelaren har dött av monstret
                Player1.losing_lives()
                if Player1.lives == 0:
                    return 'dead'

class Item():
    def __init__(self, category, name, strength, attribute, durability):
        self.category = category
        self.name = name
        self.strength = strength
        self.attribute = attribute
        self.durability = durability

    def lose_durability(self, position_in_inventory):
        self.durability -=1
        if self.durability <= 0:
            player_inventory.pop(position_in_inventory)
    
    
    def get_strength(self):
        return self.strength

    def add_items_in_inventory(self):
        print(f"\nDu har fått {self.name}")
        self.strength += rand.randint(1,20) #Slumpad bonus strength/ health effekt på föremålet.
        
        if self.category == 'Potion': #Om kategorin är potion
            if self.attribute == 'Health': #Health potions
                print(f"Som ger dig +{self.strength} HP när du dricker den")
            elif self.attribute == 'STR': #Strength potions
                print(f"Som ger dig +{self.strength} extra styrka")
        
        elif self.category == 'Ring': #Om det är en ring
            if self.attribute == 'STR': #Strength Rings
                print(f"Som ger dig +{self.strength} styrka")
            elif self.attribute == 'Health': #Health Ring
                print(f"Som ger dig +{self.strength} extra på ditt MAX HP")
        
        elif self.category == 'Sword': #Alla svärd
            print(f"Med styrkan: {self.strength}")
        
        while True:
            if len(player_inventory) < 5: #Inventory har plats för föremålet
                choice_item = input(f'''
[1] Om du vill kasta bort föremålet 
[2] Om du vill spara föremålet 
---> ''')
                if choice_item == '1': #Kasta föremålet
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2': #Om man vill spara föremålet
                    if self.category == 'Ring': 
                        if self.attribute == "Health":
                            Player1.reset_hp += self.strength #Lägger till effekten från ringen
                        elif self.attribute == "STR":
                            Player1.strength += self.strength #Lägger till effekten från ringen
                    player_inventory.append(self) #Lägger till föremål i inventory
                    break
        
            elif len(player_inventory) >= 5: #Det är fullt i spelarens inventory
                choice_item = input('''
Ditt inventory är fullt
[1] Om du vill kasta bort föremålet 
[2] Om du vill byta ut något av de items som du redan har
---> ''')
                if choice_item == '1':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '2':
                    show_inventory() #Visar spelarens inventory
                    item_number_switch = input(f'''
Vilket nummer har det föremål som du vill ta bort [1], [2], [3], [4], [5]
Tryck på valfri knapp för att gå tillbaka [X]
---> ''').lower()
                    if item_number_switch.isdigit() == True: #Kollar om det är en siffra
                        item_number_switch = int(item_number_switch) #Gör om string till integer
                        if item_number_switch > 0 and item_number_switch <=5: #Kollar om föremålet som blivit angiven finns
                            if_sure = input('''
Är du säker på att du vill byta ut detta item?
[Ja] = 1
[Nej] = 2
---> ''')
                            if if_sure == '1': #Spelaren är säker på sitt val
                                item_number_switch = int(item_number_switch)
                                player_inventory[item_number_switch-1].popping_item() #Tar bort effekt som föremålet eventuellt har
                                player_inventory.pop(item_number_switch-1) #Tar bort föremålet ur inventoryt
                                
                                if self.category == 'Ring': 
                                    if self.attribute == "Health":
                                        Player1.reset_hp += self.strength #Ökar spelarens hp som spelaren får efter död
                                    elif self.attribute == "STR":
                                        Player1.strength += self.strength #Ökar spelarens strength
                                player_inventory.append(self) #Lägger till föremålet i spelarens inventory
                                break
                        else:
                            print("Det du angav existerar ej")

    def popping_item(self):
        '''
        Funktionen tar emot föremålet som ska tas bort ur spelarens inventory, om det är en ring så tas
        ringens påverkan på strength/health bort från spelaren
        '''
        if self.category == 'Ring':
            if self.attribute == "Health": #Om attribute är 'Health'
                Player1.reset_hp -= self.strength  #Tar bort extra reset_hp som ringen ger
            elif self.attribute == "STR": #Om attribute är 'STR'
                Player1.strength -= self.strength  #Tar bort extra styrkan som ringen ger
                        

#Random Item + Room chest
def room_chest():
    print("Det är en kista!")

    while True:
        chest_item = rand.randint(1,5) #Slumpar de olika kategorier av föremål
        category_items = [] #En lista för de föremål med kategorin som har slumpats fram
        
        if chest_item == 1: #20% för en ring
            for item in all_items:
                if item.category == 'Ring':
                    category_items.append(item) #Lägger till de olika ringarna i listan
        
        elif chest_item == 2 or chest_item == 3: #40% för ett svärd
            for item in all_items:
                if item.category == 'Sword':
                    category_items.append(item) #Lägger till de olika svärd i listan
        
        elif chest_item == 4 or chest_item == 5: #40% för potion
            for item in all_items:
                if item.category == 'Potion':
                    category_items.append(item)  #Lägger till de olika potions i listan
        
        amount_in_list = len(category_items)-1 #Antal föremål med kategorin som har slumpats fram
        random_item = rand.randint(0,amount_in_list)
        
        if category_items[random_item] in player_inventory: #Om föremålet redan finns i inventoryt
            continue 
        else:  #Föremålet finns ej i inventory
            category_items[random_item].add_items_in_inventory()
            break


def meny():
    while True:
        print('''\n
    Ange [1] för information om spelaren
    Ange [2] för inventory
    Ange [3] för att stänga meny
    Ange [4] för att avsluta spel
    ''')
        chosen_number = input("---> ")
        if chosen_number == '1':
            Player1.abilities() #Visar information om spelaren
        elif chosen_number == '2':
            inventory_usage() # Visar inventory etc.
        elif chosen_number == '3':
            break   # stänger menyn
        elif chosen_number == '4': #Avsluta spel
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

#Visar inventory
def show_inventory(): 
    number = 1 #Nummer som används för nummerordning
    for item in player_inventory: 
        if item == None: #Om spelarens inventory är tomt
            break
        
        if item.attribute == 'STR': #Om föremålet har har attribute 'STR'
            if item.category == 'Sword': #Om föremålet är ett svärd
                print(f"{number}.{item.name}  ---  {item.strength} STR --- Durability: {item.durability}", sep =' ')
            
            else: #Om föremålet är ringar, skillnaden med den ovanför är + tecknet framför item.strength
                print(f"{number}.{item.name}  ---  +{item.strength} STR", sep =' ') 
        
        elif item.attribute == 'Health': #Om föremålet har attribute 'Health'
            print(f"{number}.{item.name}  ---  +{item.strength} Health", sep =' ')
        number += 1

#Användning av inventory i menyn
def inventory_usage():
    
    while True:
        if len(player_inventory) <= 0: #Om spelarens inventory är tom
            print("Det är tomt i ditt inventory")
            input("\nTryck <Enter> för att återvända till menyn")
            break
        
        show_inventory() #Visar inventory
        choice_input = input('''
    Tryck på [1] för att ta bort föremål
    Tryck på [2] för att använda potion
    Tryck på [3] för att återvända till meny
    ---> ''')
        if choice_input == '1': #Ta bort ett föremål
            item_number_switch = input('''
    Vilket nummer har det föremål som du vill ta bort?
    Tryck på valfri knapp för att gå tillbaka [X]
    ---> ''').lower()
            if item_number_switch.isdigit() == True: #Om inputen är en siffra
                item_number_switch = int(item_number_switch) #Gör om inputen till en integer
                if item_number_switch > 0 and item_number_switch <=len(player_inventory): #Kollar om spelaren anget rätt siffra
                    if_sure = input('''
Är du saker pa att du vill ta bort detta item?
[Ja] = 1
[Nej] = 2
--->''')
                    if if_sure == '1': #Spelaren är säker på sitt val
                        player_inventory[item_number_switch-1].popping_item() #Tar bort eventuella effekter som föremålet har på strength eller reset_hp
                        player_inventory.pop(item_number_switch-1) #Tar bort föremålet som spelaren valt ut

                else: 
                    print("Det du angav existerar ej")
        elif choice_input == '2':
            Player1.use_potion()               
        elif choice_input == '3':
            break


def the_room():
    '''
    Spelaren skriver in ett värde, 
    om inputen är v, m, eller h, printas det att en dörr öppnas  och returnerar chosen_input
    Om spelaren skriver in 'e' returneras det värdet också,
    '''
    
    while True:
        chosen_input = input("Ange här --> ")
        chosen_input = chosen_input.lower()
        if chosen_input == 'v':
            print("Vänster dörr öppnas")
        elif chosen_input == 'm':
            print("Dörren i mitten öppnas")
        elif chosen_input == 'h':
            print("Höger dörr öppnas")
        if chosen_input == 'v' or 'm' or 'h' or 'e':
            return chosen_input
        if chosen_input == "420": #Bypass för att få en kista direkt, inte menad att användas
            return chosen_input

def door_chance():
    '''
    returnerar ett slumpat värde mellan 1 och 3
    '''
    door_type = rand.randint(1,3)
    return door_type


def boss_monster():
    laban() #Från filen "Animationer.py"
    
    while True:
        
        print(f"Laban: Grattis {}!")
        string = f'''
            Du har lyckats med något som 
           ingen har lyckats med på 10 år. När jag var 11 dök jag
           upp här precis som du, när jag nådde nivå 10 återvände
           jag tillbaka till mitt hem. Jag hade varit borta i 
           flera dagar. När jag nådde dörren hörde jag hur min 
           familj skrattade och hade kul, som om ingenting hade
           hänt. Då insåg jag att ingen egentligen brydde sig om
           mig. Jag bestämde mig sedan för att återvända hit. Idag
           är jag 21 år gammal i människoår, mitt ultimata mål i 
           livet är att inte låta någon ta sig härifrån vid liv,
           ingen skall få uppleva lyckan jag aldrig fick känna.
    '''
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(.03)
        sleep(1)
        completion_or_death = hänga_gubbe()  #Från filen Hänga_Gubbe.py
        if completion_or_death == 'dead':
            hanging_man() #Från filen "Animationer.py"
            Player1.hp = 0 #Spelarens hp sätts till 0 pga av att spelaren blev hängd
            Player1.losing_lives()
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
        print("Skona Labans liv       [2]")
        life_or_death = input('''
        Vad väljer du?
        ---> ''')

        if life_or_death == '1':
            laban_death() #Från filen "Animationer.py"
            dead_laban() #Från filen "Animationer.py"
            return 'laban_dead'
        elif life_or_death == '2':
            laban_alive() #Från filen "Animationer.py"
            return 'laban_alive'
        else:
            print("Laban: DÖDAA MIG!!!")


def animation_door():
    '''
    printar tre dörrar + spelarens liv och hp.
    '''
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
    

boss_monster()

#               Namn STR HP RESET_HP LVL Lives
Player1 = Player('x', 20, 200, 200, 0, None)

# Category, Name, Strength/health,      Durability
item1 = Item("Sword", "Stick", 10, "STR", 10)
item2 = Item("Sword", "Lightsaber", 200, "STR", 2)
item9 = Item("Sword", "Stone Sword", 40, "STR", 4)
item10 = Item("Sword", "Gold Sword", 60, "STR", 3)
item11 = Item("Sword", "Diamond Sword", 70, "STR", 3)
item12 = Item("Sword", "Machine gun", 300, "STR", 1)
item3 = Item("Ring", "Force Ring", 25, "STR", None)
item4 = Item("Ring", "Ring of fire", 25, "STR", None)
item5 = Item("Potion", "Health Potion", 50, "Health", None)
item7 = Item("Ring", "Health Ring", 50, "Health", None)
item8 = Item("Potion", "Borogor", 80, "Health",None)

all_items = [item1, item2, item3, item4, item5, item7, item8, item9, item10, item11, item12]
#Item 6 existerar inte just nu.
#Vid tilläg av item, lägg också in det i listan ovanför.



#--------------Main Program------------------
def main():
    
    title() #Från filen "Animationer.py"
    start_game() #Från filen "Animationer.py"
    Prolog() #Från filen "Animationer.py"
    Player1.difficulty() #Bestämmer antal liv
    Player1.set_character() #Bestämmer namn på spelaren

    while True:
        animation_door()
        given_input = the_room()
        
        if given_input == 'e': #Öppnar meny
            end_game = meny()
            if end_game == True:
                break        
        
        #Vid val av en dörr
        elif given_input == 'v' or given_input == 'm' or given_input == 'h': 
            room_type = door_chance() #Slumpar mellan de tre olika dörrar
            if room_type == 1: #Rum med en kista
                room_chest() 
                input("\nTryck <Enter> för att fortsätta")
            
            elif room_type == 2: #Rum med ett monster
                if Player1.lvl >= 10: #Om spelaren är level 10 startar boss fighten när en monster dörr öppnas
                    dead_or_not = boss_monster()
                    if dead_or_not == 'dead':
                        end_game = True
                        break
                    else:
                        end_credit() #Från filen "Animationer.py"
                
                Player1.room_monster() 
                input("\nTryck <Enter> för att fortsätta") 
            
            elif room_type == 3: #Rum med en fälla
                Player1.room_trap()
                if Player1.lives <= 0:
                    end_game = True
                    break
        elif given_input == "420":
            room_chest()
            # Player1.room_monster()

    if end_game == True:
        print("LIVES LEFT: [0]")
        print("GAME OVER!")

main()
    
    

