n1 = float(input('informe um número: '))
n2 = float(input('informe outro número: '))

if n1 > n2:
    print('o maior número é {} e o menor é {}'.format(n1,n2))
elif n2 > n1:
    print('o maior número é {} e o menor é {}'.format(n2,n1))
else:
    print('os números são iguais')
