fibonacci = 1
lista = [0]
i = 0
parada = 1000000000000000000
achou = False
print("numeros da sequencia:")
while(fibonacci < parada):
  if(i == 0):
    print(0)
  aux = fibonacci + lista[i]
  lista.append(fibonacci)
  fibonacci = aux
  print(fibonacci)
  i+=1
lista.append(fibonacci)
print("____________________________")

busca = int(input('informe um numero: '))

for c in range(len(lista)):
  if (busca == lista[c]):
    print(f'o numero {busca} está na sequencia Fibonacci')
    achou = True
    break
    
    
if (achou == False):
  print(f'o numero {busca} não está na sequencia Fibonacci')


