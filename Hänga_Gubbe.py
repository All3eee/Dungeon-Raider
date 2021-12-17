import random as rand
from time import sleep

def hänga_gubbe():
    '''
    Klassisk hänga gubbe
    '''
    print('''
Laban: Det enda sättet tar dig härifrån helskinnad är om
       du lyckas lista ut det hemliga lösenordet, då bryts
       förbannelsen och jag kan inte längre hindra dig från
       att rymma.
Laban: Om du inte klarar av detta, förvandlas du också till 
       ett spöka
    ''')
    sleep(5)
    print('''
    Hänga Gubbe
    ''')
   
    word_list = ["spel","labyrint","äpple", "skelett", "hänga", "banan", 'spöke', 'monster', 'äventyrsspel', 'föremål', 'borogor', 'svärd', 'ring', 'programmering'
    ,'hej', 'brandfarlig', 'läskig', 'djurig', 'maffig', 'spindelmannen', 'spoiler', 'tjock', "gubbe", 'python', 'klass']
    
    random_number = rand.randint(0,len(word_list)-1)  #0 till listans längd ger möjlighet att lägga till ord utan problem
    the_word = word_list[random_number] #Slumpad siffra tar ut ett ord ur listan som theword är lika med
    right_guessed_words = [] #Lista över de rätt gissade bokstäver
    guesses = 10 
    amount_of_letters_right = 0
    
    for i in range(len(the_word)):
        right_guessed_words.append("_") #lägger till understreck för style :D


    while amount_of_letters_right<len(the_word): 
        print('\n',*right_guessed_words, sep =' ') #Tar bort ' ' i listan och printar de hitills gissade bokstäver
        angiven_bokstav = input("\nBokstav: ").lower()
        if angiven_bokstav in the_word:
            if angiven_bokstav in right_guessed_words: #Om bokstaven redan är angiven
                print("\nBokstaven du angav har du redan angett")
            else:
                for letter_position in range(len(the_word)): #Kollar om det finns fler av samma bokstav i ordet
                    if angiven_bokstav == the_word[letter_position]:
                        right_guessed_words.pop(letter_position)  #Tar bort understreck
                        right_guessed_words.insert(letter_position, angiven_bokstav) #Lägger till bokstav vid en specifik
                        amount_of_letters_right +=1 # +1 rätt bokstav
        else: 
            guesses -= 1
            print(f"\nDu angav fel bokstav, {guesses} antal gissningar kvar")
            if guesses == 0:
                print("Du har inga fler gissningar, nu dör du")
                return 'dead'
        
        if amount_of_letters_right == len(the_word): #Om man har haft rätt på samma antal bokstäver som det är i ordet
            print('\n',*right_guessed_words, sep =' ')
            print("Attans, du hade rätt, ordet var:", the_word)
            input("\nTryck <Enter> för att fortsätta")