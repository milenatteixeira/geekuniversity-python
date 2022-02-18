a = int(input())
b = int(input())

soma = 0
mult = 1

for numero in range(a, b+1):
    if numero % 2 == 0:
        soma += numero
    else:
        mult *= numero

print(f'soma: {soma}\nmulti: {mult}')
