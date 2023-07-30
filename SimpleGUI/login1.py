import PySimpleGUI as sg

#tema
sg.theme('ligh')

#layout da tela
layout = [
    [sg.Text('user'), sg.Input(key='user')],
    [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('salvar login')],
    [sg.Button('login')]
]

#janela
janela = sg.Window('tela de login', layout)

#ler eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'entrar':
        if valores['user'] == 'pao' and valores['senha'] == '1234':
            #tentar fazer a message box
            sg.MESSAGE_BOX_LINE_WIDTH('bem vindo!!')