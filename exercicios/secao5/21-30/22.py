idade = int(input())
tempo = int(input())

if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
    print('Aposentado')
else:
    print('Não Aposentado')
