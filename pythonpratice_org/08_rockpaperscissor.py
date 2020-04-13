#ROCK PAPER SCISSOR

inp1 = 1
inp2 = 1

s1 = 0
s2 = 0

while inp1 and inp2:
    inp1 = input('player 1:enter choice (R/P/S)').upper()
    inp2 = input('player 2:enter choice (R/P/S)').upper()
    
    if (inp1 == 'R' and inp2 == 'P') or (inp1 == 'P' and inp2 == 'S') or (inp1 == 'S' and inp2 == 'R'):
        s2 += 1
        print('player 2 wins')
        
    elif (inp2 == 'R' and inp1 == 'P') or (inp2 == 'P' and inp1 == 'S') or (inp2 == 'S' and inp1 == 'R'):
        s1 += 1
        print('player 1 wins')
    else:
        print('invalid input... enter correct choice')
     
print(f'Player 1 score: {s1}')
print(f'Player 2 score: {s2}') 
    


