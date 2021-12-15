base_maior = float(input())
base_menor = float(input())
altura = float(input())

if base_maior > 0 and base_menor > 0:
    area_trapezio = ((base_maior+base_menor) * altura)/2
    print(f'Area: {area_trapezio}')
else:
    print('Valores invalidos')
