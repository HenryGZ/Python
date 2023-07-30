somac = somapar = maior = i = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3):
  for c in range (0,3):
    matriz[l][c] = int(input(f'informe um número na posição [{l},{c}]: '))
    if matriz [l][2]:
       somac += matriz[l][2]
    if matriz [l][c] % 2 == 0:
      somapar += matriz[l][c]
    if i == 0:
      maior = matriz[0][0]
    elif matriz[l][c] > maior:
      maior = matriz[l][c]
  i += 1
print('='*40)
for celula in range (0,3):
  print(matriz[celula])
print('='*40)
print(f'a soma dos pares é igual a:  {somapar}.')
print(f'o maior número é: {maior}')
print(f'a soma da terceira coluna é: {somac}')



