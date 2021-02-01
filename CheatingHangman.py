'''
Thomas Mataconis
Cheating Hangman
'''

def guess():
    letterGuessed = input("Guess a letter: \n")
    return letterGuessed

def createPrint(printout, largestFam, letter):
    printList = []
    keys = []
    
    for char in largestFam:
        keys.append(char)
        
    for char in printout:
        printList.append(char)
        
    if letter in keys:
        for i in keys:
            
            if i == letter:
                printList[keys.index(i)] = letter
                keys[keys.index(i)] = ""
        return ''.join(printList)
    
    else:
        return printout
        
def getFams(dictAtSize, letterGuessed):  
    families = {}
    famName = []
    finalFam = {}
    sorter = []
    numWordsLeft = {}

    for word in dictAtSize:
        families[word] = ''
        for letter in word:
            if letter != letterGuessed:
                families[word] += "-"
                
            if letter == letterGuessed:
                families[word] += letter
                
    for key in families:
        famName.append(families[key])
        
    for item in famName:
        if item not in sorter:
            sorter.append(item)
    
    for item in sorter:
        finalFam[item] =  []
        for key in families:
            if families[key] == item:
                finalFam[item] += [key]
    
    for key in finalFam:
        numWordsLeft[key] = len(finalFam[key])
        
    largestFam = 0
    
    for key in numWordsLeft:
        if numWordsLeft[key] > largestFam:
            largestFam = numWordsLeft[key]
            
    for key in finalFam:
        if len(finalFam[key]) == largestFam:
            largestFam = key
            
    return largestFam, finalFam[key]    

dictionary = []
correctSize = False
dictAtSize = []
numGuesses = 0
cheat = False
didWin = False
playing = True

for line in open("dictionary.txt", "r"):
    dictionary.append(line.strip())
    
print("Welcome to (cheating) Hangman!")

while playing:
    inp = input("Enter the size of the word you wish to play with! \n")
    size = eval(inp)
    print 
    
    while correctSize is not True:
        for word in dictionary:
            if len(word) == size:
                dictAtSize.append(word)
                correctSize = True
                
        if correctSize is not True:       
            inp = input("No word fit that size! Please enter a different size. \n")
            size = eval(inp)
        
    inp = input("How many guesses do you want? \n")
    numGuesses = eval(inp)
    
    inp = input("Do you want to see the count of how many words are remaining in my dictionary? (yes / no) \n")
    if inp.strip() == "yes":
        cheat = True
    
    guessList = []
    printout = '-' * size
    print("Here is your word:", printout)
    
    letterGuessed = guess()
    
    if not letterGuessed.isalpha(): #searched on the internet how to check if a letter is in the alphabet (https://www.geeksforgeeks.org/python-string-isalpha-application/)
            print("Please enter a letter in the alphabet!")
            letterGuessed = guess()
            
    elif len(letterGuessed) != 1: 
            print("Please only enter a sigle letter")
            letterGuessed = guess()
    while letterGuessed in guessList:
                print("You already guessed that letter!")
                letterGuessed = guess()
        
    guessList.append(letterGuessed)
    
    while numGuesses != 0 and didWin is False:
        print("*" * 40)
        print()
        getFams(dictAtSize, letterGuessed)
        largestFam, dictAtWord = getFams(dictAtSize, letterGuessed)
        printout = createPrint(printout, largestFam, letterGuessed)
            
        if letterGuessed not in printout:
            numGuesses -= 1
            print("Wrong! That letter was not in the word!!! :)")
        
        else:
            print("Wow you actually got one right???")
        
        print(printout)
        print("Guesses Remaining:", numGuesses)
        print("Letters guessed: ", end = '')
        for i in guessList:
            print(i, end = ", ")
        
        print()
        if '-' not in printout:
            print("WOW you actually won! I'm very impressed!")
            didWin = True
        
        else:
            if cheat:
                print("Number of words to choose from:", len(dictAtWord))
            if numGuesses > 0:
                letterGuessed = guess()
                if not letterGuessed.isalpha(): #searched on the internet how to check if a letter is in the alphabet (https://www.geeksforgeeks.org/python-string-isalpha-application/)
                    print("Please enter a letter in the alphabet!")
                    letterGuessed = guess()
                    
                elif len(letterGuessed) != 1: 
                    print("Please only enter a sigle letter")
                    letterGuessed = guess()
                    
                while letterGuessed in guessList:
                    print("You already guessed that letter!")
                    letterGuessed = guess()
                    
                guessList.append(letterGuessed)
                
            elif numGuesses == 0:
                print("Sorry, you have lost. Although I am not suprised ;)")
        
    playAgain = input("Do you want to play again? It looks like you need the practice! mwahahaha  (y/n)\n")
    if playAgain == 'n':
        playing = False
    
