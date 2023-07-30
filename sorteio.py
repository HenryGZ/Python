from random import shuffle
alunos = []
i = 1
while i <= 8:
  alunos.append(str(input(f'time {i}: ')))
  i += 1
shuffle(alunos)
print('='*30)
print('primeiro jogo:\n')
print(alunos[0], end=' X ') 
del(alunos[0])
print(alunos[1]) 
del(alunos[1])
print('='*30)
print('segundo jogo:\n')
print(alunos[0], end=' X ') 
del(alunos[0])
print(alunos[1]) 
del(alunos[1])
print('='*30)
print('terceiro jogo:\n')
print(alunos[0], end=' X ') 
del(alunos[0])
print(alunos[1]) 
del(alunos[1])
print('='*30)
print('quarto jogo:\n')
print(alunos[0], end=' X ') 
print(alunos[1]) 

input()
