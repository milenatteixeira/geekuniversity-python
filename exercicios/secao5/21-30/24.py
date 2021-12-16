valor = float(input())
estado = input()

if estado not in ['MG', 'SP', 'RJ', 'MS']:
    print('estado inválido')

if estado == 'MG':
    valor *= 1.07
elif estado == 'SP':
    valor *= 1.12
elif estado == 'RJ':
    valor *= 1.15
elif estado == 'MS':
    valor *= 1.08

print(f'{estado}, {valor}.')
