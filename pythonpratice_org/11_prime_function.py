#prime numbers

def prime(no):
	if no == 2:
		return 1

	if no > 1:
		for i in range(2,no):	
			if no%i == 0:
				return 0
			
			else:
				return 1

			
no = int(input('enter number to check prime:'))
a = prime(no)
print('prime' if a == 1  else 'composite')
