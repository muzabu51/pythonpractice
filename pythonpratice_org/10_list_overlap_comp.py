import random as r

len1 = int(input('enter length of list 1'))
len2 = int(input('enter length of list 2'))

#for i in range(0,len1+1):
#	l1.append(r.randint(0,10))
l1 = r.sample(range(100),len1)

#for i in range(0,len2+1):
#	l2.append(r.randint(0,10))
l2 = r.sample(range(100),len2)

l3 = [i for i in l1 if i in l2]

print(l1)
print(l2)
print(l3)