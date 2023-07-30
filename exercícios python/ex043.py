dados = []
pessoas = []
pesados = []
leves = []
pesado = leve = peso = i = 0
while True:
  dados.append(str(input('nome: ')))
  dados.append(float(input('peso: ')))
  se = str(input('quer continuar? [S/N] ')).strip().upper()[0]
  pessoas.append(dados[:])
  peso = (dados[1])
  nome = (dados[0])
  if i == 0:
    leve = peso
    pesado = peso
    pesados.append(dados[:1])
    leves.append(dados[:1])
  else:
    if i == 1:
      pesados.pop()
      leves.pop()
      if peso > pesado:
        pesado = peso
        pesados.append(dados[:1])

      if peso < leve:
        leve = peso
        leves.append(dados[:1])
    else:
      if peso > pesado or peso == pesado:
        pesado = peso
        pesados.append(dados[:1])

      if peso < leve or peso == leve:
        leve = peso
        leves.append(dados[:1])
  dados.clear()
  i += 1
  if se in 'N':
    break
print(f'foram cadastradas {i} pessoas')
print(f'o mais pesado tem {pesado}, peso de: {pesados}')
print(f'o mais leve tem {leve}, peso de : {leves}')
