from random import randint
aleatorio = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('os números sorteados foram: ', end='') 
for n in aleatorio:
    print(f'{n} ', end='')
print(f'\n\no maior numero sorteado foi {max(aleatorio)}')
print(f'o menor numero sorteado foi {min(aleatorio)}')