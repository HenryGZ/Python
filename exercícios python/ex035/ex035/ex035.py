times = ('palmeiras','bragantino','athletico-PR','atlético-MG','fortaleza','bahia','santos','atlético-GO','ceará SC','corinthians'
         'fluminense','flamento','juventude','internacional','américa-MG','são paulo','sport recife', 'cuiabá','chapecoense','gremio')

print(f'5 primeiros são: {times[0:5]}')
print('='*100)
print(f'os lanternas são: {times[15:]}')
print('='*100)
print(f'os times da séria a em ordem alfabética: {sorted(times)}')
print('='*100)
print(f'o santos está na {times.index("santos") + 1}ª posição')

