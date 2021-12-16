import math

a = float(input())
b = float(input())
c = float(input())

if a != 0:
    delta = math.pow(b, 2) - 4*a*c

    if delta < 0:
        print('não há raízes')
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / 2 * a
        print(f'raiz: {x}')
    else:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print(f'raízes: {x1}, {x2}')
else:
    print('Não é equação de 2° grau.')