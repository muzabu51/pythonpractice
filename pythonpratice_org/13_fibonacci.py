fib = [0,1]
inp = int(input('Enter quantity'))

if inp <=2:
	print(fib[:inp])
else:
	for i in range(inp-2):
		fib.append(fib[-1]+fib[-2])
	print(fib)
