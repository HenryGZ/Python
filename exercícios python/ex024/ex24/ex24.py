n = int(input('informe um número: '))

contador = 0

for i in range(1, n+1):
    if n % i == 0:
        print('divisivel por {}'.format(i))
        contador += 1
    else:
        contador += 0

if contador > 2:
    print('número não é primo')
else:
    print('número primo')







