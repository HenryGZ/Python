par = 0
teste = (int(input('digite um número: ')),
         int(input('digite um número: ')),
         int(input('digite um número: ')),
         int(input('digite um número: ')))

print(f'o valor 9 apareceu {teste.count(9)} vezes')
print(f'o valor 3 apareceu {teste.count(3)} vezes')

for c in teste:
    if c %2 ==0:
        par += 1

print(f'voce digitou {par} números pares.')


