List = list(input('input numbers in list each separated by space ').split())
List = [int(i) for i in List]
List.sort()
search = int(input('element to search for '))

print('Found') if search in List else print('Not Found')

