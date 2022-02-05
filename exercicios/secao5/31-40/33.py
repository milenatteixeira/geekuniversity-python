preco = float(input())

if preco <= 50.0:
    preco *= 1.05
elif 50 < preco <= 100:
    preco *= 1.10
else:
    preco *= 1.15

if preco <= 80:
    print('Barato')
elif 80 < preco <= 120:
    print('Normal')
elif 120 < preco <= 200:
    print('Caro')
else:
    print('Muito caro')
