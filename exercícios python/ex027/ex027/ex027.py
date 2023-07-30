media = 0
idade = 0
mulheresmenos20 = 0
for i in range (1,5):
    print('='*25)

    sexo = str(input('informe o sexo da pessoa [M/F]: '))
    nome = str(input('informe o nome da pessoa: '))
    idade = int(input('informe a idade da pessoa: '))

    media += idade

    if i == 1 and sexo in 'Mm':
        nomevelho = nome
        idadevelho = idade
    else:
        if idade > idadevelho and sexo in 'Mm':
            nomevelho = nome
            idadevelho = idade
    if idade < 20 and sexo in 'Ff':
        mulheresmenos20 += 1
print('='*25)
print('o homem mais velho é {} e sua idade é de {} anos.'.format(nomevelho, idadevelho))
print('a média de idade entre o grupo é de {} anos.'.format(media / 4))
print('no grupo existem {} mulheres com menos de 20 anos.'.format(mulheresmenos20))



