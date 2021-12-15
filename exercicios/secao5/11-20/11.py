num = int(input())
soma = 0

if num > 0:
    if num // 100 > 0:
        cent = num // 100
        soma = cent
        num -= cent*100
    if num // 10 > 0:
        cent = num // 10
        soma += cent
        num -= cent * 10
    soma += num
    print(f'Soma: {soma}')
else:
    print('Numero inválido')
