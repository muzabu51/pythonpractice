size = 3  # int(input('Enter size of board '))

ho = '---'.center(5)*size
ver = "|    "

for i in range(size):
	print(ho)
	print(ver * 4)

print(('---'.center(5))*size)