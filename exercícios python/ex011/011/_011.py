nome = str(input('digite seu nome completo:')).strip()
print('nalisando seu nome...')
print('seu ome em minúsculas é {}'.format(nome.upper()))
print('seu nome em maiúsculas é {}'.format(nome.lower()))
print('seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
split = nome.split()
print('seu primeio tem {} letras'.format(len(split[0])))