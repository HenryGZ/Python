import random
print('='*50)
print('jooken pô')
print('='*50)
player = int(input('informe sua escolha: \n[0] pedra \n[1] papel \n[2] tesoura\n'))
print('='*50)
itens = ('pedra','papel','tesoura')
computador = random.randint(0, 2)
print('o jogador escolheu {}'.format(itens[player]))
print('O computador escolheu {}'.format(itens[computador]))
print('='*50)

if computador == 0:
   if player == 0:
       print('empate')
   elif player == 1:
       print('jogador venceu!!\n ಠ╭╮ಠ')
   elif player == 2:
       print('computador venceu!!\n(╯°□°)╯ ┻━┻')
   else:
       print('jogada inválida!!')
if computador == 1:
    if player == 0:
        print('computador venceu!!\n(╯°□°)╯ ┻━┻')
    elif player == 1:
        print('empate')
    elif player == 2:
        print('jogador venceu!!\n ಠ╭╮ಠ')
    else:
        print('jogada inválida!!')
if computador == 2:
   if player == 0:
       print('jogador venceu!!\n ಠ╭╮ಠ')
   elif player == 1:
       print('computador venceu!!\n(╯°□°)╯ ┻━┻')
   elif player == 2:
       print('empate')
   else:
     print('jogada inválida!!')

  