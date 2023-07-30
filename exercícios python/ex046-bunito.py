matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
  for c in range (0,3):
    matriz[l][c] = int(input(f'informe um número na posição [{l},{c}]: '))
print('='*40)
for celula in range (0,3):
  print(matriz[celula])


