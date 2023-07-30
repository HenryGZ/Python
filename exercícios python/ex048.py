from random import randint
from time import sleep
lista = []
numeros = []
jogos = int(input('informe aquantidade de jogos: '))
total = 1
while total <= jogos: 
  i = 0
  while True:
    num = randint(1,60)
    if num not in lista:
      lista.append(num)
      i += 1
    if i >= 6:
      break
  lista.sort()
  numeros.append(lista[:])
  lista.clear()
  total += 1
print('='*13,'JOGOS','='*13)
for c, l in enumerate(numeros):
  print(f'jogo {c+1}:', f'{l}')
  sleep(0.6)
print('='*33)
