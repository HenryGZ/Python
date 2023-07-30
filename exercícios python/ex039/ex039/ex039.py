lista = []
maior = 0 
menor = 0
for c in range (0, 5):
    lista.append(int(input(f'informe um número na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
           maior = lista[c]
        if lista[c] < menor:
           menor = lista[c]
print('='*50)
print(f'os valores digitados foram: {lista}')
print(f'o maior número digitado foi: {maior} nas posições: ', end='')

for i, v in enumerate(lista):
    if v == maior:
       print(f'{i}...', end='')
print()
print(f'o menor número digitado foi: {menor} nas posições: ',end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()

