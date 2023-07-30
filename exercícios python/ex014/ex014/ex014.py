num = int(input('digite um número:'))
print('''escolha, com base na legenda qual tipo de conversão voce deseja:
1- binário
2- octal
3- hexadecimal''')
op = int(input('escolha a opção: '))

if op == 1:
    print('o número escolhido em decimal é {}.'.format( bin(num) ))
elif op == 2:
    print('o número escolhido em octal é {}.'.format(oct(num)))
elif op == 3:
    print('o número escolhido em hexadecimal é {}'. format(hex(num)))