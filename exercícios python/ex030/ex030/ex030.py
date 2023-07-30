from random import randint
i = 0
while True:
    player = int(input('informe um valor: '))
    jogo = str(input('você quer par ou impar [P/I]: '))
    computador = randint(0,10)
    soma = computador + player
    print(f'o computador escolheu {computador} e o jogador escolheu {player}, total = {soma} ', end='' )
    if soma % 2 == 0 and jogo in 'Pp':
        print('ou seja PAR\n\n                   jogador venceu!!')
        print('=' * 50)
        i += 1
    elif soma % 2 == 1 and jogo in 'Ii':
        print('ou seja ÍMPAR\n\n                 jogador venceu!!')
        print('=' * 50)
        i += 1
    elif soma % 2 == 1 and jogo in 'Pp':
        print('ou seja ÍMPAR\n\n                   jogador perdeu\n')
        print(f'\no jogador ganhou {i} rodadas consecutivas.')
        print('\n-=-=-=-=-=-=-=-GAME OVER-=-=-=-=-=-=-=-')
        break
    elif soma % 2 == 0 and jogo in 'Ii':
        print('ou seja PAR\n\n                   jogador perdeu\n')
        print(f'\no jogador ganhou {i} rodadas consecutivas.')
        print('\n-=-=-=-=-=-=-=-GAME OVER-=-=-=-=-=-=-=-')
        break