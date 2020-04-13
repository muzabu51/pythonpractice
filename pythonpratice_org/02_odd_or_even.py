num = int(input('Enter a number to check odd or even'))
if num % 2 == 0 :
	print(f"{num} is an even number"+'\n')
else:
	print(f"{num} is an odd number"+'\n')

if num % 4 == 0:
	print(f'{num} is a multiple of 4'+'\n')

num, check = input('Enter two numbers to check divisibility of first number by the second').split()

if int(num) % int(check) == 0:
	print(f"{num} gets divided evenly by {check}")

else:
	print(f"{num} does not get divided evenly by {check}")