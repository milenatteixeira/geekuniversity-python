nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

media = ((nota_1 * 2) + (nota_2 *3) + (nota_3 * 5))/10

if 0.0 <= media <= 2.9:
    print('Reprovado')
elif 3 <= media <= 4.9:
    print('Recuperação')
else:
    print('Aprovado')
