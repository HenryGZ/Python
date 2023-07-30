expressao = str(input('digite uma expressão matemática entre parenteses: '))
aberto = expressao.count('(')
fechado = expressao.count(')')
if aberto == fechado:
  print('expressão válida.')
else:
  print('expressão inválida!!')