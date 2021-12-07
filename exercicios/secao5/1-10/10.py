altura = float(input())
sexo = input()

if sexo in ['F', 'f', 'Female', 'female', 'Feminino', 'feminino']:
    print(f'Peso ideal: {(62.1 * altura) - 44.7}')
elif sexo in ['M', 'm', 'Male', 'male', 'Masculino', 'masculino']:
    print(f'Peso ideal: {(72.7 * altura) - 58}')
else:
    print('Inválido')
