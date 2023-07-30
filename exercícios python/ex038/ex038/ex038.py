palavras = ('lapis','borracha','carro','caminhao','lente','computador')
for p in palavras:
    print(f'\nna paralvra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra , end=' ')
