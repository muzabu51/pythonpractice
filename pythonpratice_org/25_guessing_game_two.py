import random as r

Min, Max, count = 0, 100, 0

while 1 :

	guess = r.randint(Min, Max)
	choice = input(f'Is {guess} your number? ("Hi", "Lo", "="") ')

	if choice == 'Hi':
		Max = guess - 1

	elif choice == 'Lo':
		Min = guess + 1

	else:
		break

	count += 1

print(f'The program took {count+1} tries to guess the number')


# more optimal logic
print('better logic', end= '\n\n')
# -------------------
Min, Max, count = 0, 100, 0
guess = 50

while 1 :

	choice = input(f'Is {guess} your number? ("Hi", "Lo", "="") ')

	if choice == 'Hi':
		Max = guess - 1

	elif choice == 'Lo':
		Min = guess + 1

	else:
		break

	count += 1
	guess = r.randint(Min, Max)
print(f'The program took {count+1} tries to guess the number')