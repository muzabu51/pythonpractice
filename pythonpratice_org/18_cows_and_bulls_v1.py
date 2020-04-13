import random as r

count = 1
flag = 1
rand_no = str(r.randint(1000,9999))

while flag :
	
	bulls = 0
	cows = 0
	user_no = input("guess the 4 digit number : ")

	if user_no.isdigit() and len(user_no) == 4:
	
		if user_no == rand_no:
			flag = 0
			print(f"Congratulations. You have found the number in {count} tries")

		else:
			for i in range(0,4):
				if user_no[i] == rand_no[i] :
					cows += 1
				elif user_no[i] in rand_no:
					bulls +=1
			print("cows ", cows, "bulls", bulls)

	else:
		print("ENTER VALID 4 DIGIT NUMBER")
		count -= 1

	count += 1

		

