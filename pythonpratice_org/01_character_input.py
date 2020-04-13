
name = input('Enter your name :')
age = input('Enter your age :')
yrs_to_100 = 100 - int(age)
rep = int(input('Enter number of times you want to diplay the output'))

for i in range(0,rep):
	print(f'{name}, You will be 100 years old in {2020 + yrs_to_100}')
