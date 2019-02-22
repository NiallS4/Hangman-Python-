'''
Hangman game (Python)
22 February 2019
Niall Stapleton
'''

import sys
import word as w

def main():
	word = w.get_random_word().upper()
	guess_limit = 10
	letters = ''
	guessed_letters = []

	print('The word is:')
	print(w.show_letters(word, letters))

	while not w.all_done(word, letters) and guess_limit > 0:
		print('Guess a letter:')
		# Avoids issues with case sensitivity
		guess = input().upper()[0]

		if guess in guessed_letters:
			print('You already guessed this letter!')

		elif not w.contains_letter(word, guess) and guess not in guessed_letters:
			guess_limit -=1
			print('Not a letter! {} lives remaining.'.format(guess_limit))

		if guess not in guessed_letters:
			guessed_letters.append(guess)

		letters += guess
		print(w.show_letters(word, letters))
		print()

	if guess_limit > 0:
		print('Well done, the word was {}.'.format(word))
	else:
		print('Sorry, you lose! The word was {}.'.format(word))

if __name__ == '__main__':
	main()