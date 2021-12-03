print('#49\n')

hora = int(input())
minuto = int(input())
segundo = int(input())

print(f'{hora}:{minuto}:{segundo}')

duracao = int(input())

segundo_final = (segundo + duracao) % 60

minuto_final = (minuto + (segundo + duracao)//60) % 60

hora_final = (hora + (minuto + (segundo + duracao)//60)//60) % 24

print(f'{hora_final}:{minuto_final}:{segundo_final}')
