import os

arquivo = r"C:\Users\henry\OneDrive\Documentos\Python\exercícios python 3\pt 2 - estrutura de decisão\teste.txt"
os.path.exists(arquivo)
if os.path.exists(arquivo) == True:
    print('existe')
else:
    print('não existe')



