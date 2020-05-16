'''
tupla = ("Juan", "Pedro", "María")

for nom in tupla:
    print(nom)

palabra = "Hola"
for letra in palabra:
    print(letra)
'''

# tupla = ("Juan", "Pedro", "María")
# cont = 0
# while cont < len(tupla):
#     print(tupla[cont])
#     cont += 1

#Cargar n números y cuantos son negativos
negativo = 0
#n = int(input("Ingrese cantidad de números: "))
for i in range(300, 310):
    num = int(input("Ingrese un número: "))
    if num < 0:
        negativo += 1
print("Cantidad de negativos:",negativo)