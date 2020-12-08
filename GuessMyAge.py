def main():

	import random
	
	random_number = random.randrange(1,101)
	correct = False
	
	age = 34
	
	while  not correct:
		guess = int(input("Guess my age? "))
		if guess == age:
				print(" Yes", age, " is my age. ")

		elif guess > random_number:
					print("Your guess is to high")

		else:
				print("Your guess is to low.")
		correct = True
				
	tryAgain = input("Would you like to try again?").lower()
	if tryAgain == "yes":
		main()
	else:
		exit()
		
main()

		