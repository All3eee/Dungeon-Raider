#Denna fil är en samling för alla olika bilder/ animationer som används i programmet
#Det är här som de flesta texter som används i spelet ligger samlade i.

import sys
from time import sleep
import random as rand


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


def animation_door(player_lives, player_hp):
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
                |        LIV:{player_lives}         |
                |        HP: {player_hp}       |
                ------------------------
    ''')
  print('''
    Vänster dörr [V], Mitten dörr [M], Höger dörr [H]    
    Meny [E]  
    ''')
    

def monster_animation():
  '''
  slumpar ett tal, för att sedan printa ett visst monster, + returnar namnet på monstret
  '''
  monster_type = rand.randint(1,7)

  #Monstret Jörgen
  if monster_type == 1:
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
    print("Djuriga Jörgen har dykt upp!")
    return 'Djuriga Jörgen'
    
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
    return 'Maffiga Mumin'

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
    print("Läskiga Leffe har dykt upp!")
    return 'Läskiga Leffe'

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
    return 'Brandfarliga Bert'
  
  #Häxan Surtant
  elif monster_type == 5:
    string = '''
      -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `.  ____  | ____ _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ 
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) 
   / / / / |  |   |  |\  \  \ 
   / / // /|  |   |  |  \  \ \  
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
      '''
    print(string)
    print('Häxan Surtant har dykt upp!')
    return 'Häxan Surtant'
  
  #Fasansfulla Frank
  elif monster_type == 6:
    string = '''
             \                  /
    _________))                ((__________
   /.-------./\\    \    /    //\.---------|
  //#######//##\\   ))  ((   //##\\########\\
 //#######//###((  ((    ))  ))###\\########\\
((#######((#####\\  \\  //  //#####))########))
 \##' `###\######\\  \)(/  //######/####' `##/
  )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
          (       ``\`..'/''       )
                     \""(
                      `- )
                      / /
                     ( /
                     /\| 
                    (  \ 
                        )
                       /
                      (
                      ` 
    '''
    print(string)
    print('Fasansfulla Frank har dykt upp!')
    return 'Fasansfulla Frank'

  #Dino Danne
  elif monster_type == 7:
    string = '''
                                               ____
   ___                                      .-~. /_"-._
  `-._~-.                                  / /_ "~o\  :Y
      \  \                                / : \~x.  ` ')
       ]  Y                              /  |  Y< ~-.__j
      /   !                        _.--~T : l  l<  /.-~
     /   /                 ____.--~ .   ` l /~\ \<|Y
    /   /             .-~~"        /| .    ',-~\ \L|
   /   /             /     .^   \ Y~Y \.^>/l_   "--'
  /   Y           .-"(  .  l__  j_j l_/ /~_.-~    .
 Y    l          /    \  )    ~~~." / `/"~ / \.__/l_
 |     \     _.-"      ~-{__     l  :  l._Z~-.___.--~
 |      ~---~           /   ~~"---\_  ' __[>
 l  .                _.^   ___     _>-y~
  \  \     .      .-~   .-~   ~>--"  /
   \  ~---"            /     ./  _.-'
    "-.,_____.,_  _.--~\     _.-~
                ~~     (   _}
                        `. ~(
                          )  \
                         /,`--'~\--'

  '''
    print(string)
    print('Dino Danne har dykt upp!')
    return 'Dino Danne'


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
  for char in string: #Skriver ut en bokstav i taget
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.01)

def dead_laban():
  string = ''' 
    .-.
   .'   `.
   :x x   :
   : -    `.
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
  sleep(1)

def Prolog():
    '''
    Ber om en input, antingen 1 eller 2, skriver ut hela prolog om inputen är 1
    '''
    while True:
      chosen_input = input('''
  För att visa prolog [1]
  För att skippa prolog [2]
  ---> ''')
      
      if chosen_input == '2':
        break
      elif chosen_input == '1':
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
          "Mitt namn är Laban, du hör inte hemma här", säger den okända
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
        input("\nTryck <Enter> för att se Labans fråga")
        break

def laban_death():
  print("*SWISH*")
  sleep(1)
  
  string = '''
  
    "Jag glömde säga en sak...", yttrar Laban i sina sista andetag.
    "Genom att döda den tidigare mästaren tar du över förbannelsen"
  Du kollar på dina händer, du kan urskilja en viss transparans.
  Du kännar din kropp bli mer och mer tyngdlös, dina fötter lämnar
  marken. Förvandligen är fullständig.

  '''
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.03)
  sleep(1)
  print("*Laban dör*")
  sleep(1)

def laban_alive():
  string ='''
  Du ser ner på  marken, i stället för ett spöke ligger där en pojke.
  Du hjälper honom på fötterna.
    "Hur ska jag någonsin kunna tacka dig för att ha brutit förbannelsen!"
  säger laban med ett stort leende på läpparna. Tillsammans går Laban och
  du mot ljuset, fria från den mörka undervärlden, fria från smärta.
  
  '''
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.03)
  sleep(1) 

def text_for_hangman(player_name):
  print(f"Laban: Grattis {player_name}!")
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
  ingen skall få uppleva lyckan jag aldrig fick känna.'''
  
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.03)
  sleep(1)
  
  
  print('''
Laban: Det enda sättet tar dig härifrån helskinnad är om
       du lyckas lista ut det hemliga lösenordet, då bryts
       förbannelsen och jag kan inte längre hindra dig från
       att rymma.
Laban: Om du inte klarar av detta, förvandlas du också till 
       ett spöke, som jag.
    ''')
  sleep(5)

def hanging_man():
  string = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ \_
     |
    _|___
    '''
  print(string)

def end_credit():
  string = '''
  Tack för att du spelade detta spel!!

  Spelet är skapat av:
    Jonatan Vängborg
    Alvin Hävrén
    William Salenius
    Jonathan Lavén
  
  =)
  '''
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.09)
  sleep(1) 

