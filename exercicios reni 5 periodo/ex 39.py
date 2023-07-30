for c in range (0,8):
    numero = int(input(f'informe o {c+1}º numero: '))

    if c == 0:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = menor

print(f'o maior número é {maior} e o menor é {menor}.')