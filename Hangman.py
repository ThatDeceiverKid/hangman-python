#Simple Hangman program for practice. Connect to a database to track results maybe?

attemptsRemaining = 1
playAgain = True

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

while playAgain == True:
    print("Let's begin! \nPlease enter any integer.")
    wordChoiceInit = input()
    gameWord = init(wordChoiceInit)
    while attemptsRemaining != 0 & attemptsRemaining < 6:  #Tracks attempts, here the guessing loop is implemented
        blankString = ""
        blanks = len(gameWord)
        for i in gameWord:
            blankString += "_ " #Generating the blanks for each letter
        print(blankString)
        charChoice = input("Please pick a letter.\n")