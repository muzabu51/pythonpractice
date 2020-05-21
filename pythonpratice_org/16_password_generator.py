# importing external libraries
import string as s
import random as r

# creating pool of charcters to be selected from for password
pool = [s.ascii_uppercase, s.ascii_lowercase, s.punctuation, s.digits]

# creating function for generating the password
def generator(l):
	
	Pass = ''
	rand = lambda st, end : r.randint(st,end)
	
	for i in range(l+1):
		p_index = rand(0,3)
		length = len(pool[p_index])
		Pass = Pass + pool[p_index][rand(0,length-1)] 

	return Pass

# getting input for the function
inp = int(input('Enter preferred length of password '))

# Function output
p = generator(inp)
print(p)
