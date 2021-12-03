print('#43\n')

valor_total = float(input())
valor_desconto = valor_total * (1-0.1)
parcelas = valor_desconto/3
comissao = 0.05

print(f'Total: {valor_total}\n'
      f'Valor com desconto: {valor_desconto}\n'
      f'Valor das parcelas: {parcelas}\n'
      f'Comissão (caso a vista): {valor_desconto * comissao}\n'
      f'Comissão (caso parcelado): {valor_total * comissao}')
