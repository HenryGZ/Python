homem = 0
maior = 0
mulher = 0

while True:
    b = str(input('você quer informar mais alguem? sim ou não? ')).upper() 

    if b in 'NAONÃON': 
        print(f'dentre essas pessoas existem {homem} homens')
        print(f'dentre essas pessoas existem {mulher} mulheres')
        print(f'dentre essas pessoas existem {maior} pessoas com mais de 18 anos')
        break

    else:
        idade = int(input('informe a idade da pessoa: '))
        sexo = str(input('informe o sexo da pessoa [M/F]: ')).upper()
        print('='*30)

        if sexo in 'M' and idade > 17:
             homem += 1
             maior += 1
        elif sexo in 'M' and idade < 18:
             homem += 1
        elif sexo in 'F' and idade > 17:
             mulher += 1
             maior += 1
        elif sexo in 'F' and idade < 18:
             mulher += 1
               
            
            



