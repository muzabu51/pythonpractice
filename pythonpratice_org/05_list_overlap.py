a = [1, 1, 2, 2, 5, 9, 8, 7, 8, 99, 88]
b = [1, 1, 5, 10, 22, 98, 88]
c = []

for i in a:
    if i in b:
        c.append(i)
        
print(set(c))

