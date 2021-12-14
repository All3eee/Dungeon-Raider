import random as rand
from time import sleep

def hänga_gubbe():
    '''
    Klassisk hänga gubbe
    '''
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
    word_list = ["spel","labyrint","äpple", "skelett", "hänga", "banan", 'spöke', 'monster', 'äventyrsspel', 'föremål', 'borogor', 'svärd', 'ring', 'programmering'
    ,'hej', 'brandfarlig', 'läskig', 'djurig', 'maffig', 'spindelmannen', 'spoiler', 'tjock', "gubbe", 'python', 'klass']
    random_number = rand.randint(0,len(word_list)-1)
    theword = word_list[random_number]
    right_guessed_words = []
    guesses = 10 
    amount_of_letters_right = 0
    for i in range(len(theword)):
        right_guessed_words.append("_") #lägger till understreck för style :D


    while amount_of_letters_right<len(theword): 
        print('\n',*right_guessed_words, sep =' ')
        angiven_bokstav = input("\nBokstav: ").lower()
        if angiven_bokstav in theword:
            if angiven_bokstav in right_guessed_words:
                print("\nBokstaven du angav har du redan angett")
            else:
                for letter_position in range(len(theword)): #Kollar om det finns fler av samma bokstav i ordet
                    if angiven_bokstav == theword[letter_position]:
                        right_guessed_words.pop(letter_position)  #Tar bort understreck
                        right_guessed_words.insert(letter_position, angiven_bokstav) #Lägger till bokstav
                        amount_of_letters_right +=1
        else: 
            guesses -= 1
            print(f"\nDu angav fel bokstav, {guesses} antal gissningar kvar")
            if guesses == 0:
                print("Du har inga fler gissningar, nu dör du")
                return 'dead'
        
        if amount_of_letters_right == len(theword): #Om man har haft rätt på samma antal ord som det är i ordet
            print('\n',*right_guessed_words, sep =' ')
            print("Attans, du hade rätt, ordet var:", theword)
            input("\nTryck <Enter> för att fortsätta")