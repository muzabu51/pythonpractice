import random as r

rand_no = r.randint(1,10)
count = 0

while True:
	inp = input('Guess the number between 1 to 10 :')
	if inp == 'exit':
		break
	elif int(inp) < rand_no:
		print(f'{inp} is less than generated number')
		count += 1
	elif int(inp) > rand_no:
		print(f'{inp} is greater than generated number')
		count += 1
	elif int(inp) == rand_no:
		print('Congrats... You have found the number')
		count += 1
		print(f'You took {count} tries')
		count = 0
	

