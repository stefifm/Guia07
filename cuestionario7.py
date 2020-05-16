t = 51
while t >= -70 or t <= 50:
    t = int(input('Cargue temperatura (entre -70 y 50, por favor): '))
    if t >= -70 or t <= 50:
        print("Error")
print("Temperatura:",t)