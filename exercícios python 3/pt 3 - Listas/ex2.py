notas = []

for n in range(5):
    print(f'informe a nota {n+1}: ')
    nota = float(input())
    notas.append(nota)

notas.sort()
print(f'as notas em ordem crescente são: {notas}')