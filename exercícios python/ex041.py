num = []
par = []
impar = []
while True:
  num.append(int(input('informe um número: ')))
  se = str(input('quer continuar? [S/N]')[:1])
  if se in 'Nn':
    break
for i, v in enumerate(num):
  if v % 2 == 0:
    par.append(v)
  else:
    impar.append(v)
print('='*50)
print(f'números digitados: {num}')
print(f'entre os números digitados os pares são: {par}')
print(f'entre os números digitados os ímpares são: {impar}')