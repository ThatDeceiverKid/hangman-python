#Simple Hangman program for practice. To-Do is at the bottom

attemptsRemaining = 1
playAgain = True
blankList = []
blanks = 0

print("Welcome to Hangman!")

user = input( "Type 'run' when you are ready to play.\n")

if user.upper().strip() != "RUN":
    while user.upper().strip() != "RUN":
        print("Invalid input. Please type 'run' in order to start the game.")
        user = input()

#Core game loop and init funciton.

def init(userInt):
    attemptsRemaining = 5
    wordList = ["BEGINNER", "SIMPLIFY", "PRACTICE", "HOWEVER", "ACLIMATE"]
    if userInt is "":
        print("Default value selected, userInt was type None.")
        userInt = 1
    j = int(userInt) % 5
    wordChoice = wordList[j]

    return wordChoice

#Checking the character choice against the word, and changed the blankList accordingly.

def checkChar(char, blanks):
    preBlank = blanks
    counter = 0
    for i in gameWord:
        if gameWord[counter].upper() == char.upper():
            blankList[counter] = char.upper()
            blanks -= 1
            counter += 1
        else:
            counter += 1
    if blanks == preBlank:
        return False
    else:
        return True

while playAgain == True:
    print("Let's begin! \nPlease enter any integer.")
    wordChoiceInit = input()
    gameWord = init(wordChoiceInit)

    blanks = len(gameWord)
    for i in gameWord:
        blankList.append("_") #Generating the blanks for each letter
    print(*blankList)

    while attemptsRemaining != 0 & attemptsRemaining < 6:  #Tracks attempts, here the guessing loop is implemented

        #Had to do this twice when implementing this way so that in case the input is wrong initially, the prompt keeps asking.
        charChoice = input("Please pick a single letter.\n")
        print("Checking the word...")
        while len(charChoice) != 1:
            charChoice = input("Please pick a single letter.\n")
            print("Checking the word...")
        
        if checkChar(charChoice,blanks) != True:
            attemptsRemaining -= 1
            print("Sorry, that letter is not in the word.")
            

#To-Do:
# - Print the Hangman
# - Implement the guessing system (attemptsRemaining, error checking user character choice, etc.)
#       - Currently has an infinite loop when first letter is incorrect.
#       - Loop only iterates letter selection once before it goes back to asking for an integer,
# - Add a stop condition for the game (attemptsRemaining = 0, word guessed and they want to quit)
# - *Eventually* create a stats upload system with a database (contained data TBD) for extra practice