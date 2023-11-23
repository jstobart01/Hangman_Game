# Hangman game
# Author: Jackson Stobart

print("Welcome to my Python Hangman Game!")

# Test word for initial game play
word = "apple"
letter = ""
# print("".join(word))

letter = input("\nPlease guess a letter: ")
# print(letter)

def letter_guess(letter, word):
    if letter in word:
        print("correct")
    else:
        print("incorrect")
    
letter_guess(letter, word)

