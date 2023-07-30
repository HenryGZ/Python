from random import randint
#importando a função randint da biblioteca random

numeros = []
maior_que_5 = []
divisivel_por_3 = []

for c in range (0,20):
    numeros.append(randint(0,10))
#adicionando 20 numeros aleatórios de 0 a 10 no vetor numeros

print(f'os numeros soteados foram: {numeros}')

print('=' * 50)

print('maiores que 5: ')
for c in range (0,20):
    if numeros[c] > 5:
        maior_que_5.append(numeros[c])
print(maior_que_5)

print('=' * 50)

print('divisiveis por 3: ')
for c in range (0,20):
    if numeros[c] % 3 == 0:
        divisivel_por_3.append(numeros[c])
print(divisivel_por_3)




