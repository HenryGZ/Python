num = [[], []]
valor = 0
for c in range (1, 8):
  valor = int(input(f'digite o {c} número: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
print(f'número pares digitados: {num[0]}')
print(f'números ímpares digitados: {num[1]} ')