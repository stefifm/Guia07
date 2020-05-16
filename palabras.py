print("Contar palabras de un texto")

letras = 0 #contador de letras para que el programa no lea los espacios en
# blanco
t_p = 0 #contador del total de palabras
p = 0 #contador para saber las palabras que comienzan con p
p_ta = 0 #contador para que cuenten las palabras que contengan ta

t = False #bandera para detectar si se pasó una palabra con t
ta = False #bandera para reaccionar al paso de una a después de la t

#cadena para cargar un texto
texto = input("Cargue un texto. Finalice en un punto: ")

#inicio del ciclo for con una nueva variable llamada palabra
for palabra in texto:
    letras += 1 #apenas inicia el ciclo, letras comienza a contar
    #condicional para detectar el final de la palabra
    if palabra == " " or palabra == "," or palabra == ".":
        #Luego, si letras es mayor a 1, el total de palabras empieza a contar
        if letras > 1:
            t_p +=1
        #Si la bandera ta cambia a True, quiere decir que hubo una palabra
        # con la expresión ta y contador p_ta va contando
        if ta:
            p_ta += 1
        #letras y las banderas t y ta deben reiniciarse porque deben cargar
        # otra cadena
        letras = 0
        t = ta = False
        #continue para regresar al ciclo. Si o si hay que ponerlo
        continue
    #para saber si una palabra comienza con p, lettras debe ser igual a 1 y
    # palabra igual a p. Si se cumple, el contador p va contando
    if letras == 1 and palabra == "p":
        p += 1
    #Esta condicional sirve para detectar la expresión ta
    if palabra == "t":
        t = True
    else:
        if palabra == "a" and t:
            ta = True
        t = False
#Resultados
print("Cantidad total de palabras:",t_p)
print("Cantidad de palabras que empiezan con p:",p)
print("Cantidad de palabras con ta:",p_ta)
