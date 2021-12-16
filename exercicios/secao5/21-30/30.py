x = int(input())
y = int(input())
z = int(input())

if x < y < z:
    print(x, y, z)
elif x < z < y:
    print(x, z, y)
elif y < x < z:
    print(y, x, z)
elif y < z < y:
    print(y, z, x)
elif z < x < y:
    print(z, x, y)
elif z < y < x:
    print(z, y, x)
