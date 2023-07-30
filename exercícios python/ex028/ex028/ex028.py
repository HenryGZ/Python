numeros = 0
soma = 0
i = 0
while True: 
    n = int(input('informe um número: '))
    if n == 999:
        break
    else:
        soma += n
        numeros += 1
print(f' a soma dos números é {soma} e a quantidade de número digitados é de {numeros} números')
