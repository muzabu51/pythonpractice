a = [1,1,2,3,4,5,10,21,3,5,8,7,9]
b = []

for i in a:
	if i < 10:
		b.append(i)
print(b)
print()

num = int(input('Enter a number to output number less than it from list: '))

for j in a:
	if j < num:
		print(j, end=' ')