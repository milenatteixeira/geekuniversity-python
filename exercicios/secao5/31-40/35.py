from calendar import isleap

dia = int(input())
mes = int(input())
ano = int(input())

print(f'{dia}/{mes}/{ano}')

isValid = True
output = ''

if not (1 <= mes <= 12):
    isValid = False
    output = 'Mês inválido. '

if not (isleap(ano)) and mes == 2:
    if dia == 29:
        isValid = False
        output += 'Dia inválido. Ano bissexto. '

if isValid:
    output = 'Data válida. '

print(output)
