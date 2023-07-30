nome = str(input('qual seu nome? '))
salario = float(input('qual é seu salario {}?'.format(nome)))
vcasa = float(input('qual o valor da casa que você deseja comprar {}?'.format(nome)))
tempo = int(input('em qauntos anos você pretende pagar esse imóvel?'))

pmensal = vcasa / (tempo / 12)

if pmensal > (0.30 * salario):
    print('infelizment {}, você não poderá comprar essa casa.'.format(nome))
else:
    print('parabens {}! você poderá comprar essa casa.'.format(nome))

