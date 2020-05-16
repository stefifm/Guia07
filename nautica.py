print("Guardería naútica")

avel = 0
alan = 0
primero = True
monto_total = 0
monto_vel = 0
monto_lan =0
n = int(input("Ingrese cantidad de barcos: "))
for i in range(n):
    tipo_barco = int(input("1-Velero, 2-Lancha: "))
    nom_barco = input("Nombre del barco: ")
    monto = int(input("Monto mensual a pagar: "))
    monto_total += monto
    if tipo_barco == 1:
        avel += monto * 12
        monto_vel += monto
        if primero == True or monto > mayor:
            mayor = monto
            id = nom_barco
            primero = False
    elif tipo_barco == 2:
        alan += monto * 12
        monto_lan += monto
promedio = monto_total / n
por_v = (monto_vel * 100) / monto_total
por_l = (monto_lan * 100) / monto_total

#Resultado
print("Total anual aportado por veleros:",avel)
print("Total anual aportado por lanchas:",alan)
if primero != True:
    print("El velero",id,"es el que mayor aporte. Valor es:",mayor)
else:
    print("Nunca se ingresó un velero y no se puede determinar la mayor "
          "cuota para veleros")

print("Promedio de todos los aportantes:",promedio)
print("Porcentaje de cuota que pagan veleros:",por_v)
print("Porcentaje de cuota que pagan veleros:",por_l)