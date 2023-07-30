num = ('zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez',
       'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

ext = int(input('digite um número de 0 a 20: '))

while True:
    if ext > 20 or ext < 0:
        ext = int(input('tente novamente digitar um número de 0 a 20: '))
    else:
        break

print(f'voce digitou {num[ext]}')
  
