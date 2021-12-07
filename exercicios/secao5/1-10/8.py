nota_1 = float(input())
nota_2 = float(input())

if 0.0 <= nota_1 <= 10.0 and 0.0 <= nota_2 <= 10.0:
    print(f'Notas válidas\nNota 1 = {nota_1}\nNota 2 = {nota_2}'
          f'\nMédia = {(nota_1+nota_2)/2}')
else:
    print('Notas inválidas.')