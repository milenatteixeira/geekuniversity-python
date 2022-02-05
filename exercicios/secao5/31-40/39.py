salario_atual = float(input())
anos_servico = int(input())

print(f'Salario atual: {salario_atual}\n'
      f'Anos: {anos_servico}\n')

salario_final = salario_atual

if salario_atual <= 500.00:
    salario_final *= 1.25
elif salario_atual <= 1000.00:
    salario_final *= 1.20
elif salario_atual <= 1500.00:
    salario_final *= 1.15
elif salario_atual <= 2000.00:
    salario_final *= 1.10

if 1 <= anos_servico <= 3:
    salario_final += 100
elif 4 <= anos_servico <= 6:
    salario_final += 200
elif 7 <= anos_servico <= 10:
    salario_final += 300
elif anos_servico > 10:
    salario_final += 500

print(f'Salario final: {salario_final}.')
