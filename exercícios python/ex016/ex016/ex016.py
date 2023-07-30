from datetime import date

nascimento = int(input(print('informe seu ano de nascimento: ')))

hoje = date.today().year
idade = hoje - nascimento

if idade == 18:
    print('é hora de se alistar meu guerreiro!!')

elif idade < 18:
    print('você terá que se alistar em {}.'.format( nascimento + 18 ))

else:
    print('já passou da hora de se alistar.')


