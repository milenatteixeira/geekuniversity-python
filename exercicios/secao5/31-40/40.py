custo_fabrica = float(input())
custo_impostos = 0

if custo_fabrica < 12_000_00:
    custo_distribuidor = custo_fabrica * 0.05
elif 12_000_00 <= custo_fabrica < 25_000_00:
    custo_distribuidor = custo_fabrica * 0.10
    custo_impostos = custo_fabrica * 0.15
elif custo_fabrica >= 25_000_00:
    custo_distribuidor = custo_fabrica * 0.15
    custo_impostos = custo_fabrica * 0.20

custo_consumidor = custo_fabrica + custo_distribuidor + custo_impostos

print(f'Custo de fábrica: {custo_fabrica}\n'
      f'Custo do distribuidor: {custo_distribuidor}\n'
      f'Custo dos impostos: {custo_impostos}\n\n'
      f'Total do consumidor: {custo_consumidor}')
