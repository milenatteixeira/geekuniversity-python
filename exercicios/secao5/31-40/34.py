nota = float(input())
faltas = int(input())

conceitos = {
    'A': 'B',
    'B': 'C',
    'C': 'D',
    'D': 'E'
}


def set_conceito(conc):
    if faltas > 20:
        return conceitos.get(conc)
    return conc


if 9.0 <= nota <= 10:
    print(True)
    conceito = set_conceito('A')
if 7.5 <= nota <= 8.9:
    conceito = set_conceito('B')
if 5.0 <= nota <= 7.4:
    conceito = set_conceito('C')
if 4.0 <= nota <= 4.9:
    conceito = set_conceito('D')
if 0.0 <= nota <= 3.9:
    conceito = set_conceito('E')

print(f'{nota} -> {conceito}')
