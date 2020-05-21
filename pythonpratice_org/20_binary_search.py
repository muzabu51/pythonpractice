List = list(input('input numbers in list each separated by space ').split())
List = [int(i) for i in List]
List.sort()
search = int(input('element to search for '))

first = 0
last = len(List)-1
found = 0

while first <= last and found == 0:

	mid = int((first+last)/2)

	if List[mid] == search:
		found = 1
	
	else:
		if search < List[mid]:
			last = mid - 1
		else:
			first = mid + 1

print('Found') if found == 1 else print('Not Found')



