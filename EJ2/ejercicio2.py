#Calcular el promedio de notas de cada 
#estudiante y mostrar quién aprobó o reprobó.

estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [5, 6, 4],
    "María": [10, 9, 8],
    "Carlos": [6, 5, 6]
}

for estudiante,notas in estudiantes.items():
    sum = 0
    promedio = 0
    for nota in notas:
        sum += nota
        promedio = sum / len(notas)
        promedio = round(promedio,2)
    if promedio >= 7:
        print(f"El estudiante con nombre {estudiante} aprobo el nivel con una nota de {promedio}")
    else:
        print(f"El estudiante con nombre {estudiante} reprobo el nivel con una nota de {promedio}")
