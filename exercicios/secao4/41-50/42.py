print('#42\n')

salario = float(input())
aumento = 0.05
imposto = 0.07

print(f'Salário: {salario}\n'
      f'Salário com aumento e desconto: {(salario * (1+aumento))*(1-imposto)}')
