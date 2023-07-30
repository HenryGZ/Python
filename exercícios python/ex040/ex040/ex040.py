num = []
while True:
    num.append(int(input('escreva um número: ')))
    se = str(input('quer continuar? [S/N]'))
    if se in 'Nn':
        break
print(f'você digitou os números: {num}')
print(f'foram digitados {len(num)} números')
num.sort(reverse=True)
print(f'os números em ordem decrescente são: {num}')
if 5 in num:
    print('o número 5 foi digitado')
