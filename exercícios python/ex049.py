from random import randint
from time import sleep
from operator import itemgetter

player = {}
player['p1'] = randint(1,6)
player['p2'] = randint(1,6)
player['p3'] = randint(1,6)
player['p4'] = randint(1,6)

ranking = {}

for k,v in player.items():
  print(f'{k} tirou {v}')
  sleep(0.5)
print('§'*50)
ranking = sorted(player.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
  print(f'{i+1} lugar: {v[0]} com {v[1]}')

input()