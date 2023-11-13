#hangman the game
import random
import sys
import Pokemon
import ArcherCast
import Metro


#creating the hangman pictures
Hangman_Stages = [r"""
 +---+             
 |   |             
     |             
     | 
     |
     |           
_____|""",
r"""
 +---+             
 |   |             
 O   |             
     | 
     |
     |           
_____|""",
r"""
 +---+             
 |   |             
 O   |             
 |   | 
     |
     |           
_____|""",
r"""
 +---+             
 |   |             
 O   |             
/|   | 
     |
     |           
_____|""",
r"""
 +---+             
 |   |             
 O   |             
/|\  | 
     |
     |           
_____|""",
r"""
 +---+             
 |   |             
 O   |             
/|\  | 
/    |
     |           
_____|""", 
r"""
 +---+             
 |   |             
 O   |             
/|\  | 
/ \  |
     |           
_____|"""]

##setting the catergory and words to choose from
##Category = 'Pokemon'
##PokeWords = 'PIKACHU CHARIZARD TORTERRA BLASTOISE VENASAUR EMPOLEON INFERNAPE DARKRAI JIRACHI SHAYMIN WHOOPER QUAGSIRE WHISHCASH WISHIWASHI LATIAS LATIOS GIRATINA DIALGA PALKIA KYOGRE GROUDON RAYQUAZA'.split()
#TODO: Create multiple catergories and get user to choose one
print(''' Please select from one of the following catergories to guess from:
            1. Pokemon
            2. Archer Cast
            3. Melbourne Train Stations''')
Choice = input('> ')
if Choice == '1':
    WordsList = Pokemon.Word_List
    Category = 'Pokemon'
elif Choice == '2':
    WordsList = ArcherCast.Word_List
    Category = 'Archer Cast'
elif Choice == '3':
    WordsList = Metro.Word_List
    Category = 'Metro Train Stations'

#setting variables for a new game
def main():
    print('Welcome to Hangman the Game!')
    
    MissedLetters = []                          #for the incorrect letters/guesses
    CorrectLetters = []                         #for the correct letters/guesses
    SecretWord = random.choice(WordsList)       #choosing the word for the player to guess
    
    #main game loop
    while True:
        DrawHangman(MissedLetters, CorrectLetters, SecretWord)
        
        #letting player enter their guess
        Guess = GetPlayerGuess(MissedLetters + CorrectLetters)
        
        if Guess in SecretWord:
            CorrectLetters.append(Guess)            #adding correct guess to correct letters
            #check if player has won
            FoundAllLetters = True
            for SecretWordLetter in SecretWord:
                if SecretWordLetter not in CorrectLetters:
                    FoundAllLetters = False
                    break
            if FoundAllLetters:
                print('Correct, the secret word was: ', SecretWord)
                print('You won!')
                break                                   #breaking out of main game loop
        else:
            #incorrect guesses
            MissedLetters.append(Guess)
            #checking if the player has had too many guesses
            if len(MissedLetters) == len(Hangman_Stages) -1:                #the '-1' is because we dont count the empty gallows
                DrawHangman(MissedLetters, CorrectLetters, SecretWord)
                print('You have had too many attempts at guessing.')
                print('The word was "{}"'.format(SecretWord))
                break

def DrawHangman(MissedLetters, CorrectLetters, SecretWord):
    #Drawing the current state of our hangman as well as displaying the incorrect and correct guesses
    print(Hangman_Stages[len(MissedLetters)])
    print('The category is:', Category)
    print()
    
    #showing incorrect guesses
    print('Missed Letters: ', end='')
    for Letter in MissedLetters:
        print(Letter, end='')
    if len(MissedLetters) == 0:
        print('No missed letters yet.')
    print()
    
    #displaying the blank spaces for the secret word choosen
    Blanks = ['_']*len(SecretWord)
    
    #replacing the blanks with the correct letters
    for i in range(len(SecretWord)):
        if SecretWord[i] in CorrectLetters:
            Blanks[i] = SecretWord[i]
    
    #showing the scret word with spaces between each character
    print(' '.join(Blanks))

def GetPlayerGuess(AlreadyGuessed):
    #makes sure a single letter is entered and is not something that has been entred prior
    #asking again until player enters something valid
    while True:
        print('Guess a letter.')
        Guess = input('> ').lower()
        if len(Guess) != 1:
            print('Please only enter a single letter.')
        elif Guess in AlreadyGuessed:
            print('You have guessed this one already. Please try again.')
        elif not Guess.isascii():
            print('Please enter a LETTER!')
        else: 
            return(Guess)
        
#if program was run and not imported, run the game: 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit