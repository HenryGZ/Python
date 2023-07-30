from datetime import date

nascimento = int(input(print('informe sue ano de nascimento:')))

hoje = date.today().year
age = hoje - nascimento

if age <= 9:
    print('mirim')
elif 9 > age or age < 15:
    print('infantil')
elif 14 > age or age < 20:
    print('junior')
elif age ==20:
    print('sênior')
elif age > 20:
    print('master')
