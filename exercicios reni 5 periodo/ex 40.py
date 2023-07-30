pessoas = []
maiores = 0
menor_que_5 = 0
for c in range(0,10):
    pessoas.append(int(input(f'informe a idade da {c+1}ª pessoa: ')))

maior_idade = pessoas[0]

media = sum(pessoas) / 10

for c in enumerate(pessoas):
    if pessoas[c] > 18:
        maiores += 1

for c in enumerate(pessoas):
    if pessoas [c] < 5:
        menor_que_5 +=1

for c in enumerate(pessoas):
    if pessoas[c] > maior_idade:
        maior_idade = pessoas[c]

print('='*50)
print(f'maiores de idade: {maiores}\n')
print(f'menores que 5 anos: {menor_que_5}\n')
print(f'maior idade: {maior_idade}')

    