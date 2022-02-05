"""
Exemplo de for com a funcao 'enumerate'

nome = 'milena'
for indice, valor in enumerate(nome):
    print(nome[indice])

Execução do enumerate(nome):
((0, 'm'), (1, 'i'), (2, 'l'), (3, 'e'), (4, 'n'), (5, 'a'))
Cria uma tupla onde cada combinacao eh composto de um indice e seu valor

Tabela de emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode

"""

emoji = '\U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji}' * num)
