import random

def contains_letter(word, letter):
	for i in range(len(word)):
		if word[i] == letter:
			return True
	return False

def show_letters(word, guesses):
	locations = ''
	for i in range(len(word)):
		if contains_letter(guesses, word[i]):
			locations += word[i]
		else:
			locations += '_'
	return locations

def all_done(word, guesses):
	count = 0
	for i in range(len(word)):
		if contains_letter(guesses, word[i]):
			count += 1
	
	# Ignores whitespace
	word = word.replace(' ', '')
	if count == len(word):
		return True
	return False

def get_random_word():
	words = [
			'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
			'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
			'Illinois', 'Indiana', 'Iowa', 'Kentucky', 'Louisiana', 'Maine',
			'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
			'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
			'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
			'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
			'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
			'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
			]

	return random.choice(words)
