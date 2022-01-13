#Den här filen innehåller spelet Hänga Gubbe

import random as rand

def hänga_gubbe():
    '''
    Klassisk hänga gubbe
    '''

    print('''
---- Hänga Gubbe ----
    ''')
   
    word_list = ["spel","labyrint","äpple", "skelett", "hänga", "banan", 'spöke', 'monster', 'äventyrsspel', 'föremål', 'borogor', 'svärd', 'ring', 'programmering'
    ,'hej', 'brandfarlig', 'läskig', 'djurig', 'maffig', 'spindelmannen', 'spoiler', 'tjock', "gubbe", 'python', 'klass']
    
    random_number = rand.randint(0,len(word_list))
    the_word = word_list[random_number] #Slumpad siffra tar ut ett ord ur listan som theword är lika med

    right_guessed_words = [] #Lista över de rätt gissade bokstäver
    guesses = 12
    amount_of_letters_right = 0
    
    the_word = the_word.upper() #Gör ordet till stora bokstäver
    
    for i in range(len(the_word)):
        right_guessed_words.append("_") #lägger till understreck för style :D


    while amount_of_letters_right < len(the_word): 
        print('\n',*right_guessed_words, sep =' ') #Tar bort ' ' i listan och printar de hitills gissade bokstäver
        angiven_bokstav = input("\nBokstav: ").upper()
        if angiven_bokstav in right_guessed_words: #Om bokstaven redan är angiven
                print("\nBokstaven du angav har du redan angett")
        else:
            amount_of_times_in_word = 0 #Används som variabel för att kunna minska antal gissningar om bokstav ej finns i ordet
            for letter_position in range(len(the_word)): #Kollar om det finns fler av samma bokstav i ordet
                if angiven_bokstav == the_word[letter_position]:
                        right_guessed_words.pop(letter_position)  #Tar bort understreck
                        right_guessed_words.insert(letter_position, angiven_bokstav) #Lägger till bokstav vid en specifik
                        amount_of_letters_right +=1 # +1 rätt bokstav
                        amount_of_times_in_word += 1
            
            if amount_of_times_in_word == 0: #Om antalet gånger i ordet är lika med 0
                guesses -= 1
                print(f"\nDu angav fel bokstav, {guesses} antal gissningar kvar")
                if guesses == 0:
                    print("Du har inga fler gissningar, nu dör du")
                    return 'dead'
                       
    print('\n',*right_guessed_words, sep =' ') #Tar bort ' ' i listan och printar gissade ordet
    print("Attans, du hade rätt, ordet var:", the_word)
    input("\nTryck <Enter> för att fortsätta")
