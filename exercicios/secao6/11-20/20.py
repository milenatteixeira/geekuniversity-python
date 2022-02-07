quantidade = 0
quantidade_par = 0

while True:
    numero = int(input())

    if numero == 1000:
        break

    quantidade += 1

    if numero % 2 == 0:
        quantidade_par += 1

print(quantidade, quantidade_par)
