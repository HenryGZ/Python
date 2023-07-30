print('{:=^50}'.format('CALCULADORA DE COMPRAS'))
total = mais1000 = i = 0
barato = ' '
while True:
    print('='*50)
    nome = str(input('nome do produto: '))
    preco = float(input('preço: R$'))
    resp = ' '
    total += preco
    i += 1
    if preco > 1000:
        mais1000 += 1
    if i == 1 or preco < menorpreco:
        menorpreco = preco
        barato = nome
    while resp not in 'SN':
            resp = str(input('quer informar outro produto?[S/N]')).upper().strip()[0]
    if resp == 'N':
            print('='*50)
            print(f'valor total: {total:.2f}')
            print(f'{mais1000} produtos custam mais de 1000 reais')
            print(f'produto mais barato foi {barato} custando R${menorpreco:.2f}')
            print('Finalizando...')
            break

            


