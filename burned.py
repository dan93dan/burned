### Burned Out ###

import random
import getpass

# Request game mode
word_to_guess = int(input("There are two game modes, guess a word, or enter a number of words to guess one of them.\nYou have 7 attempts to guess the word\nWhich do you want to play?\n 1 or 2:\n"))

# Game mode 1: The user enters a single word
if word_to_guess == 1:
    word = getpass.getpass("Insert word to guess: ").lower()  # Asks the user to enter a word
    guessedWord = ['_'] * len(word)  # Create the list with underscores based on the word length

# Game mode 2: The user enters multiple words, and one is chosen randomly
elif word_to_guess == 2:
    word_bank = getpass.getpass("Insert words to guess (separated by space): ").lower().split()  # Separate words with spaces
    word = random.choice(word_bank)  # Select a random word from the list
    guessedWord = ['_'] * len(word)  # Create the list with underscores based on the word length

# Error handling in case of invalid input
else:
    print("Wrong input...")
    word = None  # Assign None to avoid errors later

# Continue if a game mode has been entered correctly
if word:
    attempts = 7  # Define the number of attempts

    while attempts > 0:  # Loop that continues as long as the player has attempts available

        print('\nCurrent word: ' + ' '.join(guessedWord))  # Display the current word with underscores

        guess = input('Guess a letter: ').lower()  # Asks the player to guess a letter and converts it to lowercase

        if guess in word:  # Check if the guessed letter is in the word
            for i in range(len(word)):  # Go through each letter of the word
                if word[i] == guess:  # If the letter in position i matches the guessed one
                    guessedWord[i] = guess  # Replace the underscore with the guessed letter
            print('Great guess!')  # Congratulate the player for guessing correctly
        else:
            attempts -= 1  # If the letter is not in the word, one attempt remains
            print('Wrong guess! Attempts left: ' + str(attempts))  # Shows how many attempts are left

        if '_' not in guessedWord:  # If there are no underscores left, the player has guessed the word
            print('\nCongratulations!! You guessed the word: ' + word)  # Congratulate the player for guessing the whole word
            break  # Exits the loop because the game is over

    # If the attempts are exhausted
    if attempts == 0:
        print(f'\nYou\'ve run out of attempts! The word was: {word}')  # Display the correct word if attempts are exhausted
