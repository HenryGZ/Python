import math
num = float(input('informe um angulo qualquer: '))

print('o seno desse angulo é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}.'.format(math.sin(math.radians(num)), math.cos(math.radians(num)), math.tan(math.radians(num))))