print('#52\n')

apostador1 = float(input())
apostador2 = float(input())
apostador3 = float(input())
premio = float(input())

total_aposta = apostador1 + apostador2 + apostador3

perc_apost_1 = (apostador1 * 100)/total_aposta
perc_apost_2 = (apostador2 * 100)/total_aposta
perc_apost_3 = (apostador3 * 100)/total_aposta

print(f'Total Premio: {premio}\n'
      f'Total apostador 1: {perc_apost_1/100 * premio}\n'
      f'Total apostador 2: {perc_apost_2/100 * premio}\n'
      f'Total apostador 3: {perc_apost_3/100 * premio}\n')
