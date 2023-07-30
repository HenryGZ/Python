nome = str(input('digite seu nome: '))

arquivo = open('teste.txt', 'w')
arquivo.write(nome)
arquivo.close