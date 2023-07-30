distancia = float(input("informe a distancia a ser percorrida: "))

if (distancia < 200):
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'o preço final da passagem será de {preco} reais')

