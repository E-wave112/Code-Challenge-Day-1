import random
#guessing game

def guess(noGuesses, Targetvalue):
	'''
	the basis of the function is to curtail the number of guesses a user can input about a number together with it's resulting differences
	'''
	for noGuesses in range(1, noGuesses+1):
		if True:
		   guess = int(input('enter your guess: '))
		if guess<Targetvalue:
			print('Too low, you are close by ' +str(abs(guess-Targetvalue)))
		elif guess>Targetvalue:
			print('Too high, you are close by ' + str(abs(guess-Targetvalue)))	
		elif guess==Targetvalue:
			print('Correct !')
			break
			
noGuesses = int(input('enter the guess limit: '))
Targetvalue = random.randint(1,100)
print(guess(noGuesses, Targetvalue))
print('Obrigado !')