import math

num = int(input())

if num < 0:
    print('Numero invalido')
else:
    print(f'Logaritmo de {num} = {math.log10(num)}')
