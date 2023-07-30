expressao = str(input('digite uma expressão: '))
pilha = []
for simbolo in expressao:
  if simbolo == '(':
    pilha.append('(')
  elif simbolo == ')':
    if len(pilha) > 0:
      pilha.pop()
    else: 
      pilha.append(')') 
      break
if len(pilha) == 0:
  print('sua expressão está correta.')
else:
  print('sua expressão está errada!!')