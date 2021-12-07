salario = float(input())
prestacao_emprestimo = float(input())

porcentagem = (prestacao_emprestimo * 100) / salario

if porcentagem > 20:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')
