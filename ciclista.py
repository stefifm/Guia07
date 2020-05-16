print("ciclistas")

n = int(input("Cantidad de competidores: "))
primero = False
tiempo_total = 0
for i in range(n):
    nom = input("Nombre del competidor: ")
    tiempo = int(input("Tiempo del competidor (en minutos): "))
    tiempo_total += tiempo
    if primero == False or tiempo < min_tiempo:
        min_tiempo = tiempo
        ganador = nom
        primero == True
print("Ganador de la carrera es:",ganador,"y su tiempo fue:",min_tiempo)

record = int(input("Tiempo récord de la carrera (en minutos): "))
if min_tiempo < record:
    print("El tiempo del ganador es superior al récord")
else:
    print("No supero el récord")
promedio = tiempo_total / n
print("Promedio de todos los ciclistas:",promedio)