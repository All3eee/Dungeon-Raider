import random as rand
from time import sleep
from Animationer import *
from Hänga_Gubbe import *
from os import system



class Player():
    '''
    En klass för att representera spelaren/ personen
    
     De olika metoder:

    __init__()
    difficulty()
    set_character()
    room_chest()
    room_trap()
    room_monster()
    boss_monster()
    battle_menu()
    losing_lives()
    show_inventory()
    inventory_usage()
    player_information()
    use_potion()
    add_health()
    delete_item
    
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
            player_inventory: list
                lista med spelarens föremål
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
        Parameter: Self (objekt)
        Den här metoden frågar spelaren vilken svårighetsgrad de vill spela på och 
        ger den ett eller tre liv beroende på svaret. (Siffra som en string)
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
        Parameter: Self (objekt)    
        Denna metod gör så att spelaren får ge namn (string) till sin karaktär (objektet Player1).
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
        Parameter: Self (objekt)
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
        Parameter: self (objekt)
        Den här metoden används när spelaren öppnar ett rum med en fälla. Funktionen gör så att skadan man tar från
        fällan är proportionelig mot spelaren LVL.
        '''
        print("\nOh no! It's a trap")
        trap_damage = rand.randint(self.lvl,7*self.lvl) #Slumpat damage baserat på spelarens lvl
        self.hp = self.hp - trap_damage
        print(f"Du tog {trap_damage} skada")
        sleep(1)
        self.losing_lives() #Om spelaren förlorar liv eller ej

    #Monster fight rummet
    def room_monster(self):
        '''
        Parameter: Self (objekt)
        Denna metod kollar först om det är laban spelaren ska möta eller ett vanligt monster sedan
        kollar den vad monster_hp ska vara baserat på self_lvl och printar monstrets namn och hp.
        Efter det så startar fighting loopen. Där läggs spelarens ringar, bas-skada (20) och skadan från 
        eventuella vapen man väljer ihop och dras från monster_hp. Om monstret överlevde så dras sedan monstrets 
        slumpade skada (som är baserad på self.lvl) från self_hp och loopen börjar om. Om monstret dog så ökar
        self.lvl med 1 och ett meddelande som informerar spelaren printas, däremot om spelaren dör och har 0 liv
        kvar, då returneras 'dead' (str)

        '''
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
            if monster_hp <= 0: #För att inte visa negativt hp
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
        '''
        Parameter: Self (objekt)
        Denna metod till en början startar spelet 'hänga gubbe' som är i en annan fil. Om spelaren har noll liv kvar
        efter att ha kört hänga gubbe så returneras 'string' (str). Om spelaren överlever hänga gubbe, kallas en metod. Om spelaren har dött i self.room_monster(), 
        då returneras dead_or_win, dvs 'dead' (str). Spelaren får sedan ett val, beroende på vad spelaren väljer ges det olika dialoger. 
        '''
    
        laban() #Från filen "Animationer.py"
        
        text_for_hangman(self.name) #Spelarens namn är med i dialogen
    
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
                break
            elif life_or_death == '2':
                laban_alive() #Från filen "Animationer.py"
                break
            else:
                print("Laban: DÖDAA MIG!!!")

    
    #Meny före strid
    def battle_menu(self):
        '''
        Parametrar: self (objekt)
        Denna funktion används i samband med att du möter ett monster som du ska döda. 
        Funttionen printar en meny där spelaren får välja mellan 3 olika alternativ om
        vad man vill göra. Du kan attackera monstret, använda en potion eller se information om spelaren.
        Om spelaren väljer att attackera monstret så kommer det i slutändan att returneras damage_of_weapon (int), 
        dvs skada som spelaren kommer att göra på monstret. Om det är tomt i self.inventory returneras spelarens styrka (int)
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
                print(f'Styrka från händer läggs på styrkan, när man använder ett vapen')
                print(f'\nStyrka från ringar: {self.strength-20}')

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
                    sword_list_strength.append(0) #Styrkan från händerna finns redan i self.strength
                    
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
            if menu_choice == "69": #Bypass för att döda monstret snabbt. Inget att bry sig om
                return 1000000

            elif menu_choice == "2":
                self.use_potion() #Använda potion
                    
            elif menu_choice == "3":
                self.player_information() #Visar information om spelaren
                continue

    
    #Förlust av liv
    def losing_lives(self):
        '''
        Parametrar: self (objekt)
        Den här metoden kollar om obejektet Player1 från klassen 'Player' 
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
        Parametrar: self (objekt)
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
        '''
        Parametrar: self (objekt)
        Denna metod står för inventoryts interkationsmeny, den undersöker om inventoryt
        är tomt eller inte sedan printar den ut inventoryt tillsammans med en rad olika
        interaktionsalternativ.
        '''
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
            if choice_input == '1': #Ta bort ett föremål
                item_number_switch = input('''
    Vilket nummer har det föremål som du vill ta bort?
    Tryck på valfri knapp för att gå tillbaka [X]
    ---> ''').lower()
                sleep(1)
                clear()
                self.delete_item(item_number_switch)
            elif choice_input == '2':
                self.use_potion()               
            elif choice_input == '3':
                break
            sleep(1)
            clear()


    #Spelarens information
    def player_information(self):
        '''
        Parameter: Self (objekt)
        Metoden tar emot objektet 'Player1' och skriver ut olika attributer som Player1 (spelaren) har.
        '''
        
        print(f'''
Namn: {self.name}
Styrka: {self.strength}
Level: {self.lvl}
Liv: {self.lives}
HP: {self.hp}
MAX HP: {self.max_hp}''')

        input("\nTryck <Enter> för att fortsätta")

    #Använda potions
    def use_potion(self):
        '''
        Parameter: self (objekt)
        När spelaren har valt att använda en potion så printar denna metod en lista på 
        alla potions tillsamans med siffror som representerar ordningen och låter sedan 
        spelaren välja vilken de vill använda eller om de vill gå tillbaka till menyn. 
        Om valet var giltigt så används drycken som valdes och dens effekt läggs till 
        på self_hp med add_health-metoden. Om spelaren inte har några potions så printas 
        istället medelandet "Du har inga potions i ditt inventory".
        '''
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
    
    #Lägga till HP
    def add_health(self, health_increase):
        '''
        Parametrar: self (objekt) & health_increase (int)
        Om self.hp (int) adderat med health_increase (int) är större än self.max_hp (int) så är self.hp
        lika med self.max_hp annars adderas health_increase på self.hp
        '''
        if self.hp + health_increase >= self.max_hp: #För att inte få högre en än max hp
            self.hp = self.max_hp
        else:
            self.hp = self.hp + health_increase #ökar hp med potionen
        print("*Drinking Noises*")
        sleep(1)
    
    
    #Tar bort föremål
    def delete_item(self,item_number):
        '''
        Parametrar: self (objekt) & item_number (str)
        Metoden kontroller om siffran är giltig, och om den är det tas föremålet bort från objektets (self) inventory
        Antingen om item_number inte är ett heltal eller om item_number är utanför det bestämda området av siffror så returneras False (boolean).
        Om spelaren är säker på sitt val returneras True (boolean) annars returneras False (boolean). 
        '''
        if item_number.isdigit() == True: #Om inputen är en siffra
            item_number = int(item_number) #Gör om inputen till en integer
            if item_number > 0 and item_number <=len(self.player_inventory): #Kollar om spelaren anget rätt siffra
                if_sure = input('''
Är du saker på ditt val?
Ja  [1]
Nej [2]
--->''')
                sleep(1)
                clear()
                if if_sure == '1': #Spelaren är säker på sitt val
                    self.player_inventory[item_number-1].popping_item() #Tar bort eventuella effekter som föremålet har på strength eller maximala hp
                    self.player_inventory.pop(item_number-1) #Tar bort föremålet som spelaren valt ut
                    return True
                else:
                    return False
            else:
                print("Det du angav existerar ej")
                return False
        else: 
            print("Det du angav existerar ej")
            return False
            
                        
 

    
class Item():
    '''
    En klass för att representera de olika föremål

    De olika metoder:

    __init__()
    lose_durability()
    add_items_in_inventory()
    add_item_effect()
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
        Parametrar: Self (objekt), postion_in_inventory (int).
        Meotden tar emot objeketet, och positionen för svärdet i inventory i form av en integer.
        Objeketets attribut 'Durbaility' subtraheras med 1 och om durabilityn är 0 tas den bort från listan 'inventory'
        genom att använda postion_in_inventory som är positionen för objektet i inventoryt
        '''
        self.durability -=1 #Förlora en durability
        if self.durability <= 0:
            Player1.player_inventory.pop(position_in_inventory) #Tar bort föremålet ur spelaren inventory
            self.durability = self.reset_durability #Durabilityn blir återställd
    

    
    #Lägga till items i inventory
    def add_items_in_inventory(self):
        '''
        Parameter: self (objekt)
        Slumpad extra effekt läggs på self.effect (int). Beroende på vad det är för föremål skrivs det ut på ett visst sätt.
        Om spelaren har mindre än 5 föremål i inventory så finns det ett antal val att välja mellan. Samma gäller för om spelaren har 5 stycken föremål
        i sitt inventory. Vissa val dyker endast upp beroende på vad det är för typ av föremål. Inget returneras i metoden.
        '''
        
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
            #Inventory har plats för föremålet
            if len(Player1.player_inventory) < 5: 
                if self.category == 'Potion':
                    print('\n[0] Om du vill dricka föremålet')
                print('''[1] Om du vill spara föremålet 
[2] Om du vill kasta bort föremålet''')
                
                choice_item = input('---> ')
                
                #Kasta föremålet
                if choice_item == '2': 
                    print("Du kastade bort föremålet")
                    break
                #Om man vill spara föremålet
                elif choice_item == '1': 
                    self.add_item_effect()
                    Player1.player_inventory.append(self) #Lägger till föremålet i spelarens inventory
                    break
                #Väljer att dricka föremålet
                elif choice_item == '0' and self.category =='Potion':
                    Player1.add_health(self.effect) #Lägger till effekt från föremålet direkt utan att behålla den i inventoryt.
                    break
                else: 
                    print("Det du angav existerar ej")
                    continue
            
            
            #Det är fullt i spelarens inventory
            elif len(Player1.player_inventory) >= 5: 
                print("\n--- Ditt inventory är fullt ---")
                
                if self.category == 'Potion':
                    print('[0] Om du vill dricka föremålet')
                print('''[1] Om du vill byta ut något av de items som du redan har
[2] Om du vill kasta bort föremålet ''')
                
                potion_in_inventory = False #Används för att se om det finns en potion i invetoryt eller ej
                
                #Skriver ut om spelaren har en potion i inventory
                for potion in Player1.player_inventory: 
                    if potion.category == 'Potion':
                        potion_in_inventory = True 
                        print('[3] Om du vill dricka en potion från ditt inventory')
                        break
        
                choice_item = input('---> ') #Spelarens val av input
                
                #Spelaren väljer att kasta föremålet
                if choice_item == '2':
                    print("Du kastade bort föremålet")
                    break
                #Om spelaren väljer att dricka föremålet
                elif choice_item == '0' and self.category =='Potion':
                    Player1.add_health(self.effect) #Lägger till effekt från föremålet direkt utan att behålla den i inventoryt.
                    break
                #Dricka potion ur inventory
                elif choice_item == '3' and potion_in_inventory == True: #Om spelaren har en potion i sitt invetory
                    Player1.use_potion() #Använda potion
                    continue
                #Byta ut något ur inventory
                elif choice_item == '1':
                    Player1.show_inventory() #Visar spelarens inventory
                    item_number_switch = input(f'''
Vilket nummer har det föremål som du vill byta ut [1], [2], [3], [4], [5]
Tryck på valfri knapp för att gå tillbaka [X]
---> ''')
                    
                    change_item = Player1.delete_item(item_number_switch)
                    if change_item == True: #Om spelaren bytt item
                        self.add_item_effect()
                        Player1.player_inventory.append(self) #Lägger till föremålet i spelarens inventory
                        break
                    
    #Lägga till Ring effekt        
    def add_item_effect(self):
        '''
        Parameter: Self
        Metoden tar emot objektet i form av self och ändrar olika attributer i objektet 
        beroende på om self.category är lika med en 'Ring' eller inte.
        '''
        if self.category == 'Ring': 
            if self.attribute == "Health":
                Player1.max_hp += self.effect #Ökar spelarens hp som spelaren får efter död
                Player1.hp += self.effect 
            elif self.attribute == "STR":
                Player1.strength += self.effect #Ökar spelarens strength
    

    #Tar bort effekt från Ring
    def popping_item(self):
        '''
        Parameter: Self
        Metoden tar emot föremålet som ska tas bort ur spelarens inventory, om det är en ring så tas
        ringens påverkan på strength/health bort från spelaren
        '''
        if self.category == 'Ring':
            if self.attribute == "Health": #Om attribute är 'Health'
                Player1.max_hp -= self.effect #Tar bort extra max hp som ringen ger
                if Player1.hp >= Player1.max_hp:
                    Player1.hp = Player1.max_hp  
            elif self.attribute == "STR": #Om attribute är 'STR'
                Player1.strength -= self.effect  #Tar bort extra styrkan som ringen ger
    
    
    


#-----Funktioner-----#


#Rensar konsol
def clear():
  '''
  Denna funktion rensar konsolen så att den inte blir klottrig.
  '''
  system("cls || clear")



#Menyval
def meny():
    '''
    Funktionen tar inte emot något argument. Funktionen används som
    en meny för att sedan kalla på andra metoder beroende på vad man väljer för input (str)
    Om spelaren väljer att avsluta spelet returneras True (boolean)
    '''
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
        elif chosen_number == '3': #Stänger Meny
            break   
        elif chosen_number == '4': #Avsluta spel
            end = input('''Är du säker på att du vill avsluta? 
Ja     [1]
Avbryt [2]
---> ''')
            if end == "1":
                print("programmet avslutas")
                sleep(0.5)
                print("3")
                sleep(0.5)
                print("2")
                sleep(0.5)
                print("1")
                return True


#Val framför dörrarna
def the_room():
    '''
    Ingen Parameter
    Spelaren skriver in ett värde, om inputen är v, m, eller h, printas det att en dörr öppnas. Beroende på vad det är för något bakom 
    dörren så kallas lite olika funktioner/ metoder. Om spelaren har dött i någon av metoderna som blir kallade, då returneras True (bool) som används sedan för avsluta spelet.
    Om spelaren vill avsluta spel returneras 'avsluta' (str).
    '''
    
    while True:
        chosen_input = input("Ange här --> ") 
        chosen_input = chosen_input.lower() #Gör små bokstäver av input

        if chosen_input == 'e': #Öppnar meny
            quit_game = meny()
            if quit_game == True: #Spelaren valde att avsluta spelet
                return 'avsluta'        
            
        #Vid val av en dörr
        elif chosen_input == 'v' or chosen_input == 'm' or chosen_input == 'h': 
            if chosen_input == 'v':
                print("Vänster dörr öppnas")
            elif chosen_input == 'm':
                print("Dörren i mitten öppnas")
            elif chosen_input == 'h':
                print("Höger dörr öppnas")
            sleep(1)
            clear()
            room_type = door_chance() #Slumpar mellan de tre olika dörrar
            if room_type == 1: #Rum med en kista
                Player1.room_chest() 
                input("\nTryck <Enter> för att fortsätta")
                break
                
            elif room_type == 2: #Rum med ett monster
                if Player1.lvl >= 10: #Om spelaren är level 10 startar boss fighten när en monster dörr öppnas
                    dead_or_not = Player1.boss_monster()
                    if dead_or_not == 'dead': #När spelaren har dött
                        return True
                    else:
                        end_credit() #Från filen "Animationer.py"
                        break 
                    
                dead_or_not = Player1.room_monster() 
                if dead_or_not == 'dead': #När spelaren har dött
                    return True
                input("\nTryck <Enter> för att fortsätta") 
                
            elif room_type == 3: #Rum med en fälla
                Player1.room_trap()
                if Player1.lives <= 0: #Om spelaren har 0 liv
                    return True
        elif chosen_input == "420": #Bypass
            Player1.room_chest()
            break

#Slumpad Dörr
def door_chance():
    '''
    returnerar ett slumpat värde mellan 1 och 3 (int)
    '''
    door_type = rand.randint(1,3)
    return door_type




#---------------- Objekt -----------------#

#                Namn,STR,HP,Max HP,LVL,Lives
Player1 = Player('x', 20, 200, 200, 0, None)


#En slumpad extra effekt läggs på 'Effect' när man får ett föremål i en kista
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



#--------------Main Program------------------#

    
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
    end_game = the_room()
    if end_game == True: #När spelaren har dött
        print("LIVES LEFT: [0]")
        print("GAME OVER!")
        break
    if end_game == 'avsluta':
        break
    sleep(1)
    clear()
    

