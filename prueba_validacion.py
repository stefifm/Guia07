print("Validación de datos")

nombre = input("Ingrese un nombre: ")
edad = -1
while edad < 0 or edad >= 120:
    edad = int(input("Ingrese su edad: "))
    if edad < 0 or edad >= 120:
        print("Error. Se pidió que fuera > 0 y menor a 120")

print("Su nombre:",nombre)
print("Su edad:",edad)