'''
GuessingGame.py
Description: A guessing game that allows a player at most 10 attempts to guess
a random integer between 0 and 100 (inclusive). After each guess the program 
will say whether the answer is too low, too high, or correct, and after 10 
guesses or one correct guess the game will end. At the end of the game the 
program will say the player has won or lost
Author: Michael Mentele
'''
import random

def evalGuess(secret_number, guess):
	'''check the guess and give feedback on the guess if incorrect'''
	if guess == secret_number:
		print('Correct! You win! Man you\'re smart...')
		return True
	elif guess > secret_number:
		print('Nice try. Too high!')
	elif guess < secret_number:
		print('Nice try. Too low!')
	else:
		print('What in the world did you guess?')


secret_number =  int(random.random() * 100)

print("Alright, I have a secret number between 0 and 100. Can you guess what it is in 10 tries?")

for n_guesses in range(10):
	guess = int(input('What\'s your guess? '))
	if guess >= 0 or guess <= 100:
		if evalGuess(secret_number, guess):
			quit()
		else:
			print('You have %s guess left.' % (9 - n_guesses))
	else:
		print('The number is between 0 and 100... remember?')