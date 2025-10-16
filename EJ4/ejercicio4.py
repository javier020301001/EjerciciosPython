#Crear un diccionario donde cada estudiante tenga el número de veces que aparece la letra "r" en todas sus actividades.

#Para cada estudiante, crear una lista de actividades en mayúsculas.

#Transformar todo en una tupla (nombre, cantidad_r, actividades_mayusculas) y ponerlo en una lista.

#Ordenar la lista por la cantidad de "r" de mayor a menor.

#Imprimir el resultado ordenado.

estudiantes = [
    ("Juan", ["correr", "dibujar"]),
    ("Ana", ["programar"]),
    ("Luis", ["programar", "leer", "bailar"])
]
dicc_actividades_r = {}
lis_estudiantes = []

for nombre,actividades in estudiantes:
    cont = 0
    lis_actividades = []
    lis_actividades_mayusculas = []

    lis_actividades.append(nombre)
    for actividad in actividades:
        cont += actividad.count("r")
    lis_actividades.append(cont)
    for actividad in actividades:
        actividad = actividad.upper()
        lis_actividades_mayusculas.append(actividad)
    lis_actividades.append(lis_actividades_mayusculas)

    tupla_estudiantes = tuple(lis_actividades)
    lis_estudiantes.append(tupla_estudiantes)
    dicc_actividades_r.setdefault(nombre,cont)


print(f"El diccionario generado es: {dicc_actividades_r}")
print(f"La tupla resultante es:{lis_estudiantes}")


aux = 0
for indice in range(len(lis_estudiantes)):
    for indice_pos in range(indice+1,len(lis_estudiantes)):
        if lis_estudiantes[indice_pos][1] < lis_estudiantes[indice][1]:
            aux = lis_estudiantes[indice]
            lis_estudiantes[indice] = lis_estudiantes[indice_pos]
            lis_estudiantes[indice_pos] = aux


print(f"La tupla resultante ordenada por el numero de veces que se repite r:{lis_estudiantes}")