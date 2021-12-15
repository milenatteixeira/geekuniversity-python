print('1. +\n2. -\n3. *\n4. /\n')
op = int(input())

x = float(input())
y = float(input())

match op:
    case 1:
        print(f'{x} + {y} = {x+y}')
    case 2:
        print(f'{x} - {y} = {x-y}')
    case 3:
        print(f'{x} * {y} = {x*y}')
    case 4:
        print(f'{x} / {y} = {x/y}')
