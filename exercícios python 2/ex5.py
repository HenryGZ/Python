n1 = int(input('informe um número: '))

print(f'a raiz quadrada desse número é de: {n1 ** (1/2)}')
print(f'\n==========Tabuada do {n1}==========')
for i in range (1,11):
    print(f'{i} X {n1} = {i*n1}')
print('saindo...')