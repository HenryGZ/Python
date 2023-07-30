
def tempo(velocidade, tamanho):
    return tamanho/velocidade

def horas (velocidade, tamanho):
    aux = (tamanho/velocidade) / 60
    return round(aux/60)

op = 1
while (op != 0): 
    print(' _____________________________________________________________________')
    print('|   opções para prosseguir:                                           |')
    print('|                                                                     |')
    print('| 1- calcular velocidade de dowload de um arquivo                     |')
    print('| 2- mostrar o tempo do dowload em horas                              |')
    print('| 0- sair                                                             |')
    print('|_____________________________________________________________________|')
    op = int(input('opção: '))

    if(op == 1):
        velocidade = float(input('informe a velocidade da sua conexão em MB/s: '))
        tamanho = float(input('informe em MB o tamanho do arquivo: '))
        print(f'o dowload irá demorar {tempo(velocidade, tamanho)} segundos ou aproximadamente {round(tempo(velocidade, tamanho) / 60)} minutos')
    elif (op == 2):
        print(f'{round(horas(velocidade, tamanho))} hora(s) aproximadamente.')
    