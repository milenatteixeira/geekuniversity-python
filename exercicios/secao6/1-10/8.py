quantidade = 0
menor = 0
maior = 0

while quantidade != 10:
    numero = int(input())

    if numero > maior:
        maior = numero
    else:
        menor = numero

    quantidade += 1

print(maior, menor)
