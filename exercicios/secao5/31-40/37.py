hora_chegada = int(input())
min_chegada = int(input())
hora_partida = int(input())
min_partida = int(input())

valores = {
    1: 1.0,
    2: 2.0,
    3: 3.4,
    4: 4.8,
    5: 6.8
}

diferenca_horas = 0
total_valor = 0.0
horas_extras = 0
partida_min = 0

if hora_chegada > hora_partida:
    diferenca_horas = 24

diferenca_horas += abs(hora_chegada-hora_partida)
diferenca_horas *= 60

if min_chegada > min_partida:
    partida_min = 60

diferenca_minutos = abs(min_chegada - partida_min)

total_horas = (diferenca_minutos + diferenca_horas)//60

if total_horas > 5:
    horas_extras = (total_horas - 5)*2

total_valor = valores.get(total_horas) + horas_extras

print(f'Chegada: {hora_chegada}:{min_chegada}\n'
      f'Partida: {hora_partida}:{min_partida}\n\n'
      f'Total horas: {total_horas}\n'
      f'Horas extras: {horas_extras}\n\n'
      f'Valor total: {total_valor}')
