import math

x = int(input())
y = int(input())
z = int(input())

print('a. Geométrica\n'
      'b. Ponderada\n'
      'c. Harmonica\n'
      'd. Aritmetica')

op = input('Opção: ')

match op:
    case 'a':
        media = math.pow(x*y*z, 1/3)
    case 'b':
        media = (x+(2*y)+3*z)/6
    case 'c':
        media = 1/((1/x)+(1/y)+(1/z))
    case 'd':
        media = (x+y+z)/3

print(f'Media: {media}')
