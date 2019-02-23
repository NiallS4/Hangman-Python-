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
	alphabet = 'A B C D E F G H I J K L M\nN O P Q R S T U V W X Y Z'

	print('The word is:')
	print(w.show_letters(word, letters))
	print()
	print(alphabet)
	print()

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
		alphabet = alphabet.replace(guess, '#')
		print(w.show_letters(word, letters))
		print()
		print(alphabet)
		print()

	if guess_limit > 0:
		print('Well done, the word was {}.'.format(word))
	else:
		print('Sorry, you lose! The word was {}.'.format(word))

if __name__ == '__main__':
	main()
