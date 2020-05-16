print("Vendedores")

flag = False
menor = None

cp1 = 0
cp2 = 0
imp1 = 0
imp2 = 0

codigo = -1
while codigo < 0 or codigo > 2:
    codigo = int(input("1-Vendedor 1, 2-Vendedor 2: "))
    if codigo < 0 or codigo > 2:
        print("Error. Elija 1 para Vendedor 1 y 2 para Vendedor 2")

while codigo !=0:
    cantidad = int(input("Cantidad de artículos vendidos: "))
    importe = int(input("Importe de artículos vendidos: "))
    if codigo == 1:
        cp1 += cantidad
        imp1 += importe
    elif codigo == 2:
        cp2 += cantidad
        imp2 += importe
        if flag == False:
            menor = importe
            flag = True
        elif importe < menor:
            menor = importe
    codigo = -1
    while codigo < 0 or codigo > 2:
        codigo = int(input("1-Vendedor 1, 2-Vendedor 2: "))
        if codigo < 0 or codigo > 2:
            print("Error. Elija 1 para Vendedor 1 y 2 para Vendedor 2")

p_imp = (imp1 + imp2) // 2

#Resultados
print("Cantidad de productos vendidos por el Vendedor 1:",cp1)
print("Cantidad de productos vendidos por el Vendedor 2:",cp2)

print("Importe total del Vendedor 1:",imp1)
print("Importe total del Vendedor 2:",imp2)
print("Importe de la menor venta del Venddedor 2:",menor)

print("Importe promedio de ambos vendedores:",p_imp)
    