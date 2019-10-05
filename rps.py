
from random import randint
player = input('rock(r), paper(p), or scissors(s)?')
print(player, 'vs', end= ' ')
chosen = randint(1,3)
#print(chosen)


if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer ='s'
  
print(computer)
if player == computer :
  print('DRAW!')
elif player =='r'and computer =='s':
    print('Player Wins!')
elif player == 'r'and computer == 'p':
  print('Congragulations, you stink!')
elif player == 'p' and computer == 'r':
  print ('Player Wins!')
elif player == 'p' and computer == 's':
  print('Great Job, you lost.')
elif player == 's' and computer == 'r':
  print ('I Win, ya lousy human!')
