distancia = float(input())
qtd_litros = int(input())

consumo = distancia/qtd_litros

if consumo < 8:
    print('Venda o carro')
elif 8 <= consumo < 14:
    print('Economico')
else:
    print('Super economico')
