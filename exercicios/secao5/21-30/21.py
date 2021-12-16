print('Escolha a opção:\n'
      '1 - Soma de 2 números.\n'
      '2 - Diferença entre 2 números (maior pelo menor)\n'
      '3 - Produto entre 2 números\n'
      '4 - Divisão entre 2 números (o denominador não pode ser zero).')

op = input('Opção: ')

x = int(input('X: '))
y = int(input('Y: '))

match op:
    case 1:
        print(f'{x} + {y} = {x+y}')
    case 2:
        if x > y:
            print(f'{x} - {y} = {x-y}')
        else:
            print(f'{y} - {x} = {y-x}')
    case 3:
        print(f'{x}*{y} = {x*y}')
    case 4:
        if x != 0 and y != 0:
            print(f'{x}/{y} = {x/y}')
