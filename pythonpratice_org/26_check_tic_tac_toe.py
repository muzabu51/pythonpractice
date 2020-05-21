game = [[2, 1, 1],
		[1, 2, 2],
		[1, 2, 2]
		]

# result = {1: 0, 2: 0} ====> maybe canbe done for version 2


def check_straight():
	
	for i in range(3):
		j = 0 
		
		if game[i][j]:
			
			# row check
			if game[i][j] == game[i][j+1] == game[i][j+2]:
				# result.__setitem__(game[i][j], result[game[i][j]]+1) ====> V2.0
				return game[i][j]

			# column check
			elif game[j][i] == game[j+1][i] == game[j+2][i]:
				# result.__setitem__(game[j][i], result[game[j][i]]+1) ====> V2.0
				return game[i][j]
			else:
				return 0

def check_diagonal():
	if game[0][0] == game[1][1] == game[2][2]:
		# result.__setitem__(game[0][0], result[game[i][j]]+1) ====> V2.0
		return game[0][0]

	elif game[0][2] == game[1][1] == game[2][0]:
		game[0][2]

	else:
		return 0

res1 = check_straight()
res2 = check_diagonal()

if res1:
	print(f'Player {res1} wins by straight match')

elif res2:
	print(f'Player {res2} wins by diagonal match')



# pseudo

# all numbers in a sub-list are same => point to corresponding user

# all numbers in same position of sub-list are same => point to corresponding user

# if any one diagonal has same 

