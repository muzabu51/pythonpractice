repeat = 'Y'
divs = []
while repeat == 'Y':
	num = int(input('enter number to check divisor'))
	for i in range(1, num+1):
		if num % i == 0:
			divs.append(i)

	print(f'divisors of {num} are ', divs)
	repeat = input('Do you want to check again ? (Y/N)').capitalize()
	print()
	if repeat == 'Y':
		divs = []

