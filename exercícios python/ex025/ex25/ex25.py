c = 0

for i in range(0,7):
    idade = int(input('digite uma idade: '))
    if idade > 21:
        c += 1

print('voce digitou {} maiores de 18 anos'.format(c))
