# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretChars = []
    for c in secretWord:
        if c not in secretChars:
            secretChars.append(c)
        
    for c in lettersGuessed:
        if c in secretChars:
            secretChars.remove(c)

    if not secretChars:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretChars = list(secretWord)
    for c in secretChars:
        if c not in lettersGuessed:
            secretChars[secretChars.index(c)] = '_'

    return ' '.join(secretChars)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allCharList = list(string.ascii_lowercase)
    for c in lettersGuessed:
        if c in allCharList:
            allCharList.remove(allCharList[allCharList.index(c)])

    return ''.join(allCharList)

def makeGuess(guessesLeft, availableLetters):
    print('You have', guessesLeft, 'guesses left.')
    print('Available letters:', availableLetters)
    guess = input('Please guess a letter: ')

    if guess not in string.ascii_letters:
        print('Only letters a-z allowed!')
        print('-------------')
        makeGuess(guessesLeft, availableLetters)

    return guess

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    word = secretWord
    lettersGuessed = []
    guessesLeft = 8
    availableLetters = getAvailableLetters(lettersGuessed)
    winner = False

    # start game
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(word), 'letters long.')
    print('-------------')

    while guessesLeft > 0:
        guess = makeGuess(guessesLeft, availableLetters).lower()

        # check if character already guessedadd char to lettersGuessed
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', getGuessedWord(word, lettersGuessed))
            print('-------------')
        else:
            # add guessed character to list of guessed characters
            lettersGuessed.append(guess)
            # check if guess was in word
            if guess in secretWord:
                print('Good guess:', getGuessedWord(word, lettersGuessed))
                print('-------------')
            else:
                print('Oops! That letter is not in my word:', getGuessedWord(word, lettersGuessed))
                print('-------------')
                guessesLeft -= 1

        availableLetters = getAvailableLetters(lettersGuessed)

        # check if correct word was guessed
        if isWordGuessed(word, lettersGuessed):
            winner = True
            guessesLeft = 0
    
    if winner:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was', word + '.')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
