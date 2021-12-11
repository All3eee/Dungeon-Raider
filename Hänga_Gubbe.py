import random as rand
from time import sleep


def hänga_gubbe():
    print("Laban: AHA, trodde du verkligen att du skulle kunna rymma!!")
    sleep(3)
    print('''
    Laban: Om du klarar Hänga gubbe så kanske jag låter dig komma ut!
    Laban: Om du inte klarar det, är det du som blir hängd!!
    ''')
    sleep(5)
    print('''
    Hänga Gubbe
    ''')
    ord = ["lol","bruh","hej", "tjena", "hänga", "banan", "gubbe", 'lose', 'hej']
    slumptal = rand.randint(0,len(ord)-1)
    theword = ord[slumptal]
    ordet_understreck = []
    gissningar = 10 
    x = 0
    for i in range(len(theword)):
        ordet_understreck.append("_")


    while x<len(theword): 
        print(ordet_understreck)
        angiven_bokstav = input("\nBokstav: ").lower()
        if angiven_bokstav in theword:
            for j in range(len(theword)):
                if angiven_bokstav == theword[j]:
                    ordet_understreck.pop(j)
                    ordet_understreck.insert(j, angiven_bokstav)
                    x+=1
        else: 
            gissningar -= 1
            print(f"Du angav fel bokstav, {gissningar} antal gissningar kvar")
            if gissningar == 0:
                print("Du har inga fler gissningar, nu dör du")
                return 'dead'
        
        if x == len(theword):
            print(ordet_understreck)
            print("Attans, du hade rätt, ordet var:", theword)
            input("\nTryck <Enter> för att fortsätta")
