num = []
par = []
impar = []
#declaração dos vetores

for c in range (0,6):
  num.append(int(input('informe um número: ')))
  #jogando o numero dentro de um vetor diretamente sem variavel auxiliar


for i, v in enumerate(num):
  if v % 2 == 0:
    par.append(v)
  else:
    impar.append(v)

#o enumarate percorre o vetor, ele entende o tamanho dele e ele é o critério de parada
#para o for, e nesse tipo de declaração a primeira variavel i é o contador e a variavel j
# recebe o conteudo presente na casa i dentro do vetor

print('='*50)
print(f'números digitados: {num}')
print(f'entre os números digitados os pares são: {par}')
print(f'entre os números digitados os ímpares são: {impar}')