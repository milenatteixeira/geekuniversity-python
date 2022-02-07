quantidade = int(input())
maior = 0
maior_quantidade = 0

while quantidade != 0:
    numero = int(input())

    if numero == maior:
        maior_quantidade += 1

    if numero > maior:
        maior = numero
        maior_quantidade = 1

    quantidade -= 1

print(maior, maior_quantidade)
