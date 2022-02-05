from calendar import isleap

dia = int(input())
mes = int(input())
ano = int(input())

ano_atual = 2022

ultimo_dia = {
    1: 31,
    2: 28 if not isleap(ano) else 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

print(f'{dia}/{mes}/{ano}')

if ano <= ano_atual:
    if 1 <= mes <= 12:
        if 1 <= dia <= ultimo_dia.get(mes):
            print('Data válida.')
        else:
            print('Data inválida. Dia inexistente nesse mês.')
    else:
        print('Data inválida. Mês inexistente.')
else:
    print('Data inválida. Ano maior que o atual.')
