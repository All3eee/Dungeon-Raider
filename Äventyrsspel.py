import random as rand
from time import sleep
from Animationer import *
from Hänga_Gubbe import *
from os import system

#Rensar konsol
def clear():
  '''
  Denna funktion rensar konsolen så att den inte blir klottrig.
  '''
  system("cls || clear")


class Player():
    '''
    En klass för att representera spelaren/ personen
    

    '''
    
    def __init__(self, name, strength, hp, max_hp, lvl, lives):
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
            max_hp : int
                Maximala hp som spelaren har
            lvl : int
                nivå/level som spelaren är på
            lives : int
                antal liv som spelaren har kvar
        """
        self.name = name
        self.strength = strength
        self.hp = hp
        self.max_hp = max_hp
        self.lvl = lvl
        self.lives = lives
        self.player_inventory = [] #Spelarens inventory

    def difficulty(self):
        '''
    Den här funktionen frågar spelaren vilken svårighetsgrad de vill spela på och 
    ger den ett eller tre liv beroende på svaret.
        '''
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
        '''
    Denna funktion gör så att spelaren får ge namn till sin karaktär (objektet Player1).
        '''
        print("\nLaban: Vad heter du?")
        self.name = input("Ange ditt namn ->: ")
        print(f'''
Laban: Jasså, så du heter {self.name}.
       Du ser ut att ha varit med om en hel del.
        ''')

    #Random Item + Room chest
    def room_chest(self):
        '''
    Denna metod avgör vilket item du får från en kista genom att först välja kategori
    och sedan ett item från den kategorin.
        '''
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
            
            if category_items[random_item] in self.player_inventory: #Om föremålet redan finns i inventoryt
                continue 
            else:  #Föremålet finns ej i inventory
                category_items[random_item].add_items_in_inventory()
                break
    
    #Rummet med en fälla
    def room_trap(self):
        '''
    Den här funktionen används när spelaren öppnar ett rum med en fälla. Funktionen gör så att skadan man tar från
    fällan är proportionelig mot spelaren LVL.
        '''
        print("\nOh no! It's a trap")
        trap_damage = rand.randint(self.lvl,7*self.lvl) #Slumpat damage baserat på spelarens lvl
        self.hp = self.hp - trap_damage
        print(f"Du tog {trap_damage} skada")
        sleep(1)
        self.losing_lives() #Om spelaren förlorar liv eller ej

    def room_monster(self):
        if self.lvl >= 10: #Vid level 10 slåss spelaren mot laban
            laban()
            monster_hp = 500 #Labans HP är alltid 500 hp
            monster_namn = 'Laban'
        else: 
            monster_namn = monster_animation() #Från filen "Animationer.py"
            monster_hp = 120 + 10*self.lvl #HP på monstret ökar för varje level
            
        print(f"{monster_namn} har {monster_hp} HP")
        
        while True:
            damage_on_monster = self.battle_menu()

            input(f"\nTryck <Enter> för att attackera {monster_namn}")
            sleep(1)
            clear()
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
            damage1 = rand.randint(2*self.lvl,20 + 18*self.lvl) 
            self.hp = self.hp - damage1 
            print(f"\nDu tog {damage1} damage")
            if self.hp <= 0: 
                self.hp = 0 #För att inte visa negativ hp
            print(f"Du har {self.hp} Hp kvar")
            if self.hp <= 0: #Om spelaren har dött av monstret
                self.losing_lives()
                if self.lives == 0:
                    return 'dead'

    #Boss monster                
    def boss_monster(self):
    
        laban() #Från filen "Animationer.py"
        
        text_for_hangman(self.name)
    
        while True:
            completion_or_death = hänga_gubbe()  #Hänga Gubbe sätts igång; Från filen Hänga_Gubbe.py
            if completion_or_death == 'dead':
                hanging_man() #Från filen "Animationer.py"
                self.hp = 0 #Spelarens hp sätts till 0 pga av att spelaren blev hängd
                self.losing_lives()
                if  self.lives == 0:
                    return 'dead'
                else:
                    print("Du förlora ett liv, du får en chans till att köra hänga gubbe")
                    continue
            else:
                break
        
        print("BOSSS FIGHT PÅ GÅNG")
        sleep(1)
        dead_or_win = self.room_monster()
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

    
    #Meny före strid
    def battle_menu(self):
        '''
    Denna funktion används i samband med att du möter ett monster som du ska döda. 
    Funttionen printar en meny där spelaren får välja mellan 3 olika alternativ om
    vad man vill göra. Du kan attackera monstret, använda en potion eller se information om spelaren.
        '''
        while True:
            menu_choice = input('''
[1] Attackera
[2] Använda potion
[3] Information om spelare
---> ''')
            clear()
            if menu_choice == "1":
                number = 1 #Används för rangordning
                sword_list_strength = [] #List för de olika svärd i inventory
                sword_list = []

                print(f'\nStyrka från ringar: {self.strength}')
                print(f'Styrka från händer läggs på, när man använder ett vapen')
                for item in self.player_inventory:
                    if item.category == 'Sword': #Om kategorin är ett svärd
                        print(f"{number}.{item.name}  ---  {item.effect} STR --- Durability: {item.durability}", sep =' ') #Skriver ut föremålet
                        sword_list.append(item)
                        sword_list_strength.append(item.effect) #Lägger till föremålets STR i listan
                        number += 1
                
                if number == 1:
                    print("Du har inget vapen och måste slåss med händerna!")
                    return self.strength
    
                else:     
                    print(f"{number}.Händer  --- 20 STR", sep =' ') #Skriver ut föremålet
                    sword_list.append('Händer')
                    sword_list_strength.append(0)
                    
                    while True:
                        weapon_choice = input("Vilket nummer har vapnet som du vill använda? --> ")
                        if weapon_choice.isdigit() == True: #Kollar om inputen är siffror
                            weapon_choice = int(weapon_choice) #Gör om från string till integer
                            if weapon_choice > 0 and weapon_choice <= len(sword_list_strength):
                                
                                #damage_of_weapon är all damage som läggs på, skadan från vapnet, och spelarens styrka
                                damage_of_weapon = sword_list_strength[weapon_choice - 1] + self.strength
                                
                                choosen_weapon = sword_list[weapon_choice - 1] #Det valda vapnet (objekt)
                                position_in_inventory = 0
                                if choosen_weapon == 'Händer':
                                    pass
                                else:      
                                    for the_weapon in self.player_inventory:
                                        if the_weapon == choosen_weapon:
                                            break
                                        position_in_inventory += 1
                                    choosen_weapon.lose_durability(position_in_inventory)
                                return damage_of_weapon
                            else:
                                print("Det du angav existerar ej")
                                
                        else:
                            print("Det du angav existerar ej")
            if menu_choice == "69": #Bypass för att döda monstret snabbt
                return 1000000

            elif menu_choice == "2":
                self.use_potion() #Använda potion
                    
            elif menu_choice == "3":
                self.player_information() #Visar information om spelaren
                continue

    
    #Förlust av liv
    def losing_lives(self):
        '''
    Den här funktionen kollar om obejektet Player1 från klassen 'Player' 
    har 0 eller mindre hp och tar då bort ett liv och återställer spelarens
    hp om spelaren fortfarande har liv kvar.
        '''
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
    
        #Visar inventory
    def show_inventory(self):
        '''
        Denna metod printar en lista med dem föremål som du har i ditt inventory. Spelarens föremål
        printas i en numrerad lista samt att varje enskilt föremål har information om deras olika egenskaper.
        '''
        print('------ INVENTORY ------')
        number = 1 #Nummer som används för nummerordning
        for item in self.player_inventory: 
            if item == None: #Om spelarens inventory är tomt
                break
            
            if item.attribute == 'STR': #Om föremålet har har attribute 'STR'
                if item.category == 'Sword': #Om föremålet är ett svärd
                    print(f"{number}.{item.name}  ---  {item.effect} STR --- Durability: {item.durability}", sep =' ')
                
                else: #Om föremålet är ringar, skillnaden med den ovanför är + tecknet framför item.effect
                    print(f"{number}.{item.name}  ---  +{item.effect} STR", sep =' ') 
            
            elif item.attribute == 'Health': #Om föremålet har attribute 'Health'
                if item.category == 'Ring':
                    print(f"{number}.{item.name}  ---  +{item.effect} MAX HP", sep =' ')
                else:
                    print(f"{number}.{item.name}  ---  +{item.effect} Health", sep =' ')
            number += 1

        #Användning av inventory i menyn
    def inventory_usage(self):
    
        while True:
            if len(self.player_inventory) <= 0: #Om spelarens inventory är tom
                print("Det är tomt i ditt inventory")
                input("\nTryck <Enter> för att återvända till menyn")
                clear()
                break
        
            self.show_inventory() #Visar inventory
            choice_input = input('''
    Tryck på [1] för att ta bort föremål
    Tryck på [2] för att använda potion
    Tryck på [3] för att återvända till meny
    ---> ''')
            sleep(1)
            clear()
            if choice_input == '1': #Ta bort ett föremål
                item_number_switch = input('''
    Vilket nummer har det föremål som du vill ta bort?
    Tryck på valfri knapp för att gå tillbaka [X]
    ---> ''').lower()
                sleep(1)
                clear()
                if item_number_switch.isdigit() == True: #Om inputen är en siffra
                    item_number_switch = int(item_number_switch) #Gör om inputen till en integer
                    if item_number_switch > 0 and item_number_switch <=len(self.player_inventory): #Kollar om spelaren anget rätt siffra
                        if_sure = input('''
Är du saker pa att du vill ta bort detta item?
[Ja] = 1
[Nej] = 2
--->''')
                        sleep(1)
                        clear()
                        if if_sure == '1': #Spelaren är säker på sitt val
                            self.player_inventory[item_number_switch-1].popping_item() #Tar bort eventuella effekter som föremålet har på strength eller maximala hp
                            self.player_inventory.pop(item_number_switch-1) #Tar bort föremålet som spelaren valt ut

                    else: 
                        print("Det du angav existerar ej")
            elif choice_input == '2':
                self.use_potion()               
            elif choice_input == '3':
                break



    def player_information(self):
        
        print(f'''
Namn: {self.name}
Styrka: {self.strength}
Level: {self.lvl}
Liv: {self.lives}
HP: {self.hp}
MAX HP: {self.max_hp}''')

        input("\nTryck <Enter> för att fortsätta")


    def use_potion(self):
        potion_value_list = [] #Lista för potions i inventoryt
        potion_position_in_inventory = []  #Används för att veta platserna för de olika potions
        number_of_potion = 1 #Används för rangordning
        number_in_inventory = 0 #Används för att veta var potions är i inventory
        for item in self.player_inventory:
            if item.category == 'Potion':
                print(f"{number_of_potion}.{item.name}  ---  +{item.effect} Health", sep =' ')
                potion_value_list.append(item.effect) #Lägger in effekten på de olika potions
                            
                #Lägger till platserna för de olika potions i Player inventory
                potion_position_in_inventory.append(number_in_inventory)
                number_of_potion += 1
            
            number_in_inventory +=1
        if number_of_potion == 1:
            print("\nDu har inga potions i ditt inventory")
            
        else:
            potion_choice = input('''
Vilket nummer har den potion som du vill använda? -->
Tryck på valfri knapp för att gå tillbaka [X]
---> ''')

            if potion_choice.isdigit() == True: #Om potion_choice är en siffra
                potion_choice = int(potion_choice) 
                if potion_choice <= len(potion_value_list) and potion_choice > 0: 
                    health_increase = potion_value_list[potion_choice- 1] #Tar ut effekten på den valda potion
                    
                    self.add_health(health_increase)

                    position = potion_position_in_inventory[potion_choice-1]
                    self.player_inventory.pop(position) #Tar bort potion från inventory efter användning
                else:
                    print("Det du angav existerar ej")
            else:
                print("Det du angav existerar ej")
    

    def add_health(self, health_increase):
        if self.hp + health_increase >= self.max_hp: #För att inte få högre en än max hp
            self.hp = self.max_hp
        else:
            self.hp = self.hp + health_increase #ökar hp med potionen
        print("*Drinking Noises*")
        sleep(1)
 

    
class Item():
    '''
    En klass för att representera de olika föremål

    De olika metoder:

    __init__()
    lose_durability()
    add_items_in_inventory()
    popping_item()

    '''
    
    def __init__(self, category, name, effect, attribute, durability, reset_durability):
        """
        Alla nödvändiga attributer

        Parametrar
        ----------
            category : str
                Typ av föremål
            name : str
                Namnet på föremålet
            effect : int
                styrkan eller health effekt beroende på item
            attribute : str
                variabel som används för att särskilja items med health eller styrke effekt
            durability : int
                Antal gånger som föremålet är använt innan den går sönder (endast för catergory 'Sword')
            reset_durability: int
                Används för att återställa self.durability
        """
        self.category = category
        self.name = name
        self.effect = effect
        self.attribute = attribute
        self.durability = durability
        self.reset_durability = reset_durability

    #Förlorar durability
    def lose_durability(self, position_in_inventory):
        '''
        Funktionen tar emot positionen för svärdet i inventory i form av en integer.
        Durbailityn subtraheras med 1 och om durabilityn är 0 tas den bort från listan inventory
        '''
        self.durability -=1
        if self.durability <= 0:
            Player1.player_inventory.pop(position_in_inventory)
            self.durability = self.reset_durability
    

    def add_items_in_inventory(self):
        print(f"\nDu har fått {self.name}")
        self.effect += rand.randint(1,20) #Slumpad bonus strength/ health effekt på föremålet.
        
        if self.category == 'Potion': #Om kategorin är potion
            if self.attribute == 'Health': #Health potions
                print(f"Som ger dig +{self.effect} HP när du dricker den")
            elif self.attribute == 'STR': #Strength potions
                print(f"Som ger dig +{self.effect} extra styrka")
        
        elif self.category == 'Ring': #Om det är en ring
            if self.attribute == 'STR': #Strength Rings
                print(f"Som ger dig +{self.effect} styrka")
            elif self.attribute == 'Health': #Health Ring
                print(f"Som ökar ditt MAX HP med {self.effect} hp")
        
        elif self.category == 'Sword': #Alla svärd
            print(f"Med styrkan: {self.effect} --- Durability:{self.durability}")
        
        while True:
            if len(Player1.player_inventory) < 5: #Inventory har plats för föremålet
                if self.category == 'Potion':
                    print('\n[0] Om du vill dricka föremålet')
                choice_item = input(f'''[1] Om du vill spara föremålet 
[2] Om du vill kasta bort föremålet
---> ''')
                if choice_item == '2': #Kasta föremålet
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '1': #Om man vill spara föremålet
                    pass #Resten av koden finns längre ned
                elif choice_item == '0' and self.category =='Potion':
                    Player1.add_health(self.effect)
                    break
                else: 
                    print("Det du angav existerar ej")
                    continue
            
            elif len(Player1.player_inventory) >= 5: #Det är fullt i spelarens inventory
                print("\n--- Ditt inventory är fullt ---")
                if self.category == 'Potion':
                    print('[0] Om du vill dricka föremålet')
                choice_item = input('''
[1] Om du vill byta ut något av de items som du redan har
[2] Om du vill kasta bort föremålet 
---> ''')
                if choice_item == '2':
                    print("Du kastade bort föremålet")
                    break
                elif choice_item == '0' and self.category =='Potion':
                    Player1.add_health(self.effect)
                    break
                elif choice_item == '1':
                    Player1.show_inventory() #Visar spelarens inventory
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
                                Player1.player_inventory[item_number_switch-1].popping_item() #Tar bort effekt som föremålet eventuellt har
                                Player1.player_inventory.pop(item_number_switch-1) #Tar bort föremålet ur inventoryt
                                
                        else:
                            print("Det du angav existerar ej")
                            continue
                    else:
                        print("Det du angav existerar ej")
                        continue
            
            if if_sure == '1' or choice_item == '1': #Skriver denna här för att annars skulle den behövas på två ställen
                if self.category == 'Ring': 
                    if self.attribute == "Health":
                        Player1.max_hp += self.effect #Ökar spelarens hp som spelaren får efter död
                        Player1.hp += self.effect 
                    elif self.attribute == "STR":
                        Player1.strength += self.effect #Ökar spelarens strength
                Player1.player_inventory.append(self) #Lägger till föremålet i spelarens inventory
                break


    def popping_item(self):
        '''
        Funktionen tar emot föremålet som ska tas bort ur spelarens inventory, om det är en ring så tas
        ringens påverkan på strength/health bort från spelaren
        '''
        if self.category == 'Ring':
            if self.attribute == "Health": #Om attribute är 'Health'
                Player1.max_hp -= self.effect #Tar bort extra max hp som ringen ger
                if Player1.hp >= Player1.max_hp:
                    Player1.hp == Player1.max_hp  
            elif self.attribute == "STR": #Om attribute är 'STR'
                Player1.strength -= self.effect  #Tar bort extra styrkan som ringen ger
            
                        


#-----Funktioner-----#

#Menyval
def meny():
    while True:
        clear()
        print('''\n
    Ange [1] för information om spelaren
    Ange [2] för inventory
    Ange [3] för att stänga meny
    Ange [4] för att avsluta spel
    ''')
        chosen_number = input("---> ")
        if chosen_number == '1':
            Player1.player_information() #Visar information om spelaren
        elif chosen_number == '2':
            Player1.inventory_usage() # Visar inventory etc.
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



def the_room():
    '''
    Spelaren skriver in ett värde, 
    om inputen är v, m, eller h, printas det att en dörr öppnas  och returnerar chosen_input
    Om spelaren skriver in 'e' returneras det värdet också, Det returnerade värdet är en string
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




#---------------- Objekt -----------------#

#                Namn,STR,HP,Max HP,LVL,Lives
Player1 = Player('x', 20, 200, 200, 0, None)

#         Category, Name, Effect, Attribute, Durability x2
item1 = Item("Sword", "Stick", 10, "STR", 10, 10)
item2 = Item("Sword", "Lightsaber", 200, "STR", 2, 2)
item9 = Item("Sword", "Stone Sword", 40, "STR", 5, 5)
item10 = Item("Sword", "Gold Sword", 60, "STR", 4, 4)
item11 = Item("Sword", "Diamond Sword", 70, "STR", 3, 3)
item12 = Item("Sword", "Machine gun", 300, "STR", 1, 1)
item8 = Item("Potion", "Borogor", 80, "Health",None, None)
item5 = Item("Potion", "Health Potion", 50, "Health", None, None)
item6 = Item("Potion", "Slurp Juice", 60, "Health", None, None)
item7 = Item("Ring", "Health Ring", 50, "Health", None, None)
item3 = Item("Ring", "Force Ring", 25, "STR", None, None)
item4 = Item("Ring", "Ring of fire", 25, "STR", None, None)
item13 = Item("Ring", "Shield", 30, "Health", None, None) 

#Lista för alla items
all_items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13]
#Vid tilläg av item, lägg också in det i listan ovanför.



#--------------Main Program------------------#
def main():
    end_game = False #Variabel som används för att stänga av spelet helt
    
    title() #Från filen "Animationer.py"
    start_game() #Från filen "Animationer.py"
    Prolog() #Från filen "Animationer.py"
    clear()
    Player1.difficulty() #Bestämmer antal liv
    sleep(0.2)
    clear()
    Player1.set_character() #Bestämmer namn på spelaren
    sleep(2.5)
    while True:
        clear()
        animation_door(Player1.lives, Player1.hp)
        given_input = the_room()
        sleep(1)
        clear()
        if given_input == 'e': #Öppnar meny
            quit_game = meny()
            if quit_game == True:
                break        
        
        #Vid val av en dörr
        elif given_input == 'v' or given_input == 'm' or given_input == 'h': 
            sleep(1)
            clear()
            room_type = door_chance() #Slumpar mellan de tre olika dörrar
            if room_type == 1: #Rum med en kista
                Player1.room_chest() 
                input("\nTryck <Enter> för att fortsätta")
            
            elif room_type == 2: #Rum med ett monster
                if Player1.lvl >= 10: #Om spelaren är level 10 startar boss fighten när en monster dörr öppnas
                    dead_or_not = Player1.boss_monster()
                    if dead_or_not == 'dead':
                        end_game = True
                        break
                    else:
                        end_credit() #Från filen "Animationer.py"
                        break 
                
                dead_or_not = Player1.room_monster() 
                if dead_or_not == 'dead':
                    end_game = True
                    break
                input("\nTryck <Enter> för att fortsätta") 
            
            elif room_type == 3: #Rum med en fälla
                Player1.room_trap()
                if Player1.lives <= 0:
                    end_game = True
                    break
        elif given_input == "420":
            Player1.room_chest()
            # Player1.room_monster()

    if end_game == True:
        print("LIVES LEFT: [0]")
        print("GAME OVER!")

main()