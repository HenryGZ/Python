cinquenta = vinte = dez = um = 0
valor = float(input('Valor a ser sacado: R$'))
print('='*50)
while True:
    if valor >= 50:
                valor = valor - 50
                cinquenta += 1

    elif valor >= 20:
                valor = valor - 20
                vinte +=1

    elif valor >= 10:
                valor = valor - 10
                dez += 1
    elif valor >= 1:
                valor = valor - 1
                um += 1
    elif valor == 0:              
        print(f'{cinquenta} cédulas de 50 reais')
        print(f'{vinte} cédulas de 20 reais')
        print(f'{dez} cédulas de 10 reais')
        print(f'{um} cédulas de 1 real')
        print('{:=^50}'.format('FIM DA OPERAÇÃO'))
        break