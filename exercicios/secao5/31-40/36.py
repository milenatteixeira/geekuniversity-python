valor_venda = float(input())
valor_total = 0.0
perc_comiss = 14

if valor_venda >= 100_000_00:
    valor_total = 700
    perc_comiss = 16
elif 80_000_00 <= valor_venda < 100_000_00:
    valor_total = 650
elif 60_000_00 <= valor_venda < 80_000_00:
    valor_total = 600
elif 40_000_00 <= valor_venda < 60_000_00:
    valor_total = 550
elif 20_000_00 <= valor_venda < 40_000_00:
    valor_total = 500
elif valor_venda < 20_000_00:
    valor_total = 400

valor_total += valor_venda * perc_comiss

print(f'Valor total: {valor_total}')
