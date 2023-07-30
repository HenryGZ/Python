valor = float(input('valor do balaio: '))
total_gasto = 0
while True:
  print('=' * 50)
  nome = str(input('nome: '))
  qtd = float(input('quantidade de balaios: '))
  total = qtd * valor
  print(f'pagamento: {total}')
  print('=' * 50)
  total_gasto += total
  condicao = str(input('quer continuar? [S/N] ')).upper()
  if condicao in 'NNAONÃO':
    break
print(f'total pago: {total_gasto}')
  