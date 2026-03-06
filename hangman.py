# Name: Snovi Patel
# Hangman.py

'''
Purpose: The game selects a random word from a list of words in a file.
The player tries to guess the word by guessing one letter at a time.
The player can make up to seven wrong guesses before losing the game.
'''


import random # Imports random library


# Purpose: Reads a list of words from a file,
# strips extra whitespace, and returns them as a list of lowercase words.
# Input: None
# Output: A list of words (strings) read from the file,
# with whitespace removed and all converted to lowercase.

def readWords():
    # Open the words.txt file in read mode
    with open("words.txt", "r") as file:
        words = [line.strip().lower() for line in file if line.strip()]
        
    return words # Return the list of words




# Purpose: Chooses a random word from the list of words.
# Input: A list of words (strings)
# Output: A randomly selected word from the list

def randomWord(words):
    return random.choice(words)



# Purpose: Prompts the player to enter a letter guess, checks for invalid input, and ensures the letter hasn't been guessed before.
# Input: A list of previously guessed letters (list of strings)
# Output: The guessed letter (string)

def getGuess(guessedLetters):
    while True: # Loop until a valid guess is entered
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha(): # Check if the input is a single letter
            print("Please enter one letter only.")
            
        elif guess in guessedLetters: # Check if the letter has already been guessed
            print("You already guessed that letter.")
            
        else:
            guessedLetters.append(guess) # Add the guess to the list of guessed letters
            return guess




# Purpose: Generates a string of blanks and guessed letters to display to the player.
# Input: The secret word (string) and the list of guessed letters (list of strings)
# Output: A string showing blanks for unguessed letters and the correct letters where guessed.

def blanks(word, guessedLetters):
    result = ""
    
    for letter in word:# Loop through each letter in the word
        
        if letter in guessedLetters: # If the letter has been guessed
            result += letter + " " # Add the letter to the result with a space
            
        else:
            result += "_ " # Add a blank for unguessed letters
            
    return result.strip()





# Purpose: Checks if the game has been won by the player.
# Input: The string representing the current blanks (string)
# Output: True if all letters have been guessed, False otherwise

def gameWon(blanksString):
    return "_" not in blanksString # Return True if there are no blanks left




# Purpose: Tests all the functions.
# Input: None
# Output: Prints the results of testing each function

def test():
    # Write words to the file
    with open("words.txt", "w") as file:
        file.write("keyboard\nhangman\npython\n")

    print("1. Testing readWords:")
    wordList = readWords() # Call readWords to load the words from the file
    print("Words loaded:", wordList) # Display the loaded words

    print("\n2. Testing randomWord:")
    secret = randomWord(wordList) # Call randomWord to choose a secret word
    print("Random secret word:", secret) # Display the selected secret word

    guessedLetters = ["e", "a", "n"] # Sample guessed letters
    print("\n3. Testing blanks:")
    current = blanks(secret, guessedLetters) # Generate the blanks string
    print("Blanks shown:", current) # Shows the blanks with guessed letters

    print("\n4. Testing gameWon:")
    print("Game won?", gameWon(current)) # Check if the game is won and display the result

    print("\n5. Testing getGuess (try entering a new letter):")
    newGuess = getGuess(guessedLetters) # Prompt the user to enter a new guess
    print("Your guess:", newGuess) # Display the guessed letter
    print("All guessed letters so far:", guessedLetters) # Display the list of all guessed letters so far
    




# Purpose: Starts the game, controls the flow of the game.
# Input: None
# Output: Prints the game status, including the word with blanks, wrong guesses, and whether the player won or lost.

def playGame():
    print("Welcome to Hangman!")
    
    words = readWords() # Read the list of words# Read the list of words
    word = randomWord(words) # Select a random word
    
    guessedLetters = [] # Initialize the list of guessed letters
    
    wrongGuesses = [] # wrong guesses

    while True:  # Loop until the game ends
        # Display the current word with blanks and guessed letters
        print("\nWord:", blanks(word, guessedLetters))
        # Display the wrong guesses
        print("Wrong guesses:", " ".join(wrongGuesses))
        # Display how many guesses are left
        print("Guesses left:", 7 - len(wrongGuesses))

        guess = getGuess(guessedLetters) # Get the player's guess

        if guess in word: # If the guess is correct
            print("Good guess!")
            
        else: # If the guess is incorrect
            print("Wrong guess!")
            
            if guess not in wrongGuesses: # If the guess hasn't been recorded before
                wrongGuesses.append(guess) # Add the wrong guess to the list
                
        # Check if the game is won

        if gameWon(blanks(word, guessedLetters)):
            print("\nYou won! The word was:", word)
            break
        
        # Check if the player has made 7 wrong guesses
        elif len(wrongGuesses) >= 7:
            print("\nYou lost! The word was:", word)
            break