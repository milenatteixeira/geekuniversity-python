notas = []
soma = 0

while True:
    nota = int(input())

    if 10 <= nota <= 20:
        notas.append(nota)
    else:
        break

media = [soma := soma + x for x in notas][-1]/len(notas)

print(f'Notas: {notas}')
print(f'Média aritmética das notas: {media:.2f}')
