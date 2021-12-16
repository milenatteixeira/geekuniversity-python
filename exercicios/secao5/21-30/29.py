import random

cont = 0
for _ in range(5):
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    print(f'Qual é a soma de {x}+{y}?')
    result = int(input())

    if result == (x + y):
        cont += 1

    print(f'A soma é {x+y}\n\n')

print(f'Total de acertos: {cont}')