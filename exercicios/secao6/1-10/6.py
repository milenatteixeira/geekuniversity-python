quantidade = 0
soma = 0
media = 0

while quantidade != 10:
    numero = int(input())
    soma += numero
    quantidade += 1

media = soma/quantidade
print(media)
