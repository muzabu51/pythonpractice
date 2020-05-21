s = list(input('Enter sentence to be reversed ').split(' '))
ss = []

#reverse by loop
for i in s:
	ss.insert(0, i)

#reverse by slicing
s = str(s[::-1])

print(s)
print(ss)


