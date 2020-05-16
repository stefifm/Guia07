print("Secuencia de impares")

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a < b:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i)
else:
    if a > b:
        for c in range(a, b + 1, -1):
            if c % 2 != 0:
                print(c)