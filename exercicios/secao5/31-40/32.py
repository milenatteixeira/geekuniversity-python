codigo = int(input())
qtd = int(input())

cardapio = {
    100: {
        'Cachorro Quente',
        1.2
    },
    101: {
        'Bauru Simples',
        1.3
    },
    102: {
        'Bauru com Ovo',
        1.5
    },
    103: {
        'Hamburguer',
        1.2
    },
    104: {
        'Cheeseburguer',
        1.7
    },
    105: {
        'Suco',
        2.2
    },
    106: {
        'Refrigerante',
        1
    }
}

if codigo in cardapio:
    produto = list(cardapio.get(codigo))
    total = produto[1] * qtd

    print(f'{produto[0]}\nTotal: {total}')
else:
    print('Produto indisponível.')