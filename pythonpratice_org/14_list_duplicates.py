
def ListDuplicateSet(inp):
	return list(set(inp)) 

def ListDupNoSet(inp):
	# index error in logic
	# for i in range(len(inp)-2):
	# 	if not inp.index(i) == inp.index(inp[-1]):
	# 		chk_list = inp[0:i]+inp[i+1::]
	# 	if inp[i] in chk_list:
	# 		inp.remove(inp[i])
	# return inp

	for i in inp:
		count = inp.count(i)
		if count > 1:
			inp.remove(i)
	return inp

l_in = list(input('Enter list of items separated by space').split(' '))
l_out = ListDuplicateSet(l_in)
print(l_out)

l_ou1 = ListDupNoSet(l_in)
print('without using set ', l_ou1)