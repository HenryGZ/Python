while True:
    n = int(input('qual tabuada você deseja ver? '))

    if n < 0:
        print('fechando o programa...')
        break
    else:
        for c in range(1,11):
            print(f'{c} X {n} = { c * n}')
        print('='*20)

        
