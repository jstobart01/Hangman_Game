# Hangman game
# Author: Jackson Stobart
# Rev 1.1 - 2023-11-25

print("Welcome to my Python Hangman Game!")

# Test word for initial game play
word = "apple"
letter = ""
player_guess = []
# print("".join(word))

letter = input("\nPlease guess a letter: ")
# print(letter)


def letter_guess(letter, word):
    if player_string != word:
        if letter in word:
            global player_guess
            player_guess.append(letter)
            print(player_guess)
            player_string = str(player_guess)
        else:
            print("incorrect") 
    else:
        print("Congrats")

#player_string = str(player_guess)

#if player_string == word:
   # print("correct word")
# else:
    
