import sys
from time import sleep
import random as rand

def animation_dr():
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

def monster_animation():
    monster_type = rand.randint(1,4)

    #Monstret Jörgen
    if monster_type == 1:
      print("Djuriga Jörgen har dykt upp!")
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
|     \     \|_A_,
|      \     ____)
\       \  /`
      \(
                """
      print(string)
    
    #Mumin
    elif monster_type == 2:
      string = '''
                .   ,
               .';_.';
              .       `.
              .     _   _
             .     :x: :x:--._
            .       "   "     `.
           .                   :
          .        ._         .'
          .          `"""----"
          .           `.
         .              .
         .   .  `.       .
         .    `.  `.      .
 .       .      ` . `.    .
'M;      .         "`     .
 `     .' .               '
  `"--"    ,    __,..-   '  .
          .   .'     `.   `' ;
          `.   `,      `.  .'
            ".-'         `' 
      '''
      print(string)
      print("Maffiga Mumin har dykt upp!")
    
    #Monstret leffe
    elif monster_type == 3:
      string ='''
               _.---._
             .'       `.
             :)       (:
             \ (@) (@) /
              \   A   /
               )     (
               \"""""/
                `._.'
                 .=.
         .---._.-.=.-._.---.
        / ':-(_.-: :-._)-:` |
       / /' (__.-: :-.__) `\ |
      / /  (___.-` '-.___)  \ |
     / /   (___.-'^`-.___)   \ |
    / /    (___.-'=`-.___)    \ |
   / /     (____.'=`.____)     \ |
  / /       (___.'=`.___)       \ |
 (_.;       `---'.=.`---'       ;._)
 ;||        __  _.=._  __        ||;
 ;||       (  `.-.=.-.'  )       ||;
 ;||       \    `.=.'    /       ||;
 ;||        \    .=.    /        ||;
 ;||       .-`.`-._.-'.'-.       ||;
.:::\      ( ,): O O :(, )      /:::.
|||| `     / /'`--'--'`\ \     ' ||||
          / /           \ \      

      '''
      print(string)
      print("Läskiga leffe har dykt upp!")
    
    #Monstret Bert
    elif monster_type == 4:
      string = '''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \     |   ( '        )(    )
      \    |  \.  _.__ ____( .  |
       \  /|  .(   .'  /\  '.  )
        \( |.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '| .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
      '''
      print(string)
      print("Brandfarliga Bert har dykt upp!")


def laban():
  string = ''' 
    .-.
   .'   `.
   :g g   :
   : O    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;:-'
    '''
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.03)

 

def title():
  string = '''

██████████████████████████▀████████████████████████████████████████████████████████
█▄─▄▄▀█▄─██─▄█▄─▀█▄─▄█─▄▄▄▄█▄─▄▄─█─▄▄─█▄─▀█▄─▄███▄─▄▄▀██▀▄─██▄─▄█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█
██─██─██─██─███─█▄▀─██─██▄─██─▄█▀█─██─██─█▄▀─█████─▄─▄██─▀─███─███─██─██─▄█▀██─▄─▄█
▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
'''
  print(string)

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
    
def chest_animation():
  string = '''
  ******************************************************************************
            |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/[TomekK]
  *******************************************************************************
  '''
  print(string)