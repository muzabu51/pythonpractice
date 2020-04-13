def firstlast(a):
	b=[]
	b.append(a[0])
	b.append(a[-1])
	return b

a = [23,44,89,78,98,12]
out = firstlast(a)
print(out)