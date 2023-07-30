numeros = []
#declaração de vetor em python

for c in range (0,7):
    aux = int(input("informe um numero inteiro: "))
    numeros.append(aux)
    #adicionando o numero dentro do vetor ( vetor.append(numero))

print(f"a soma da lista é {sum(numeros)}")