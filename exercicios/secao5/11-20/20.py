a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print('Triângulo equilátero.')
elif a == b or a == c or b == c:
    print('Triângulo isósceles.')
else:
    print('Triângulo escaleno.')
