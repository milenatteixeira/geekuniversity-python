num = int(input())

if num % 3 == 0:
    print(f'{num} é divisivel por 3')
if num % 5 == 0:
    print(f'{num} é divisivel por 5')
if num % 3 == 0 and num % 5 == 0:
    print(f'{num} é divisivel por 3 e por 5')
else:
    print(f'{num} não é divisivel por 3 e por 5')