
#Combinar conjuntos y tuplas 
# para crear un registro único de 
# materias cursadas sin repetir.

juan = ("Matemáticas", "Arte", "Química", "Programación")
ana = ("Química", "Inglés", "Programación", "Arte")
pedro = ("Historia", "Física", "Matemáticas", "Arte")

materias_juan = set(juan)
materias_ana = set(ana)
materias_pedro = set(pedro)

materias_unidas = materias_juan.union(materias_ana).union(materias_pedro)
print(f"Estas son las materias cursadas por todos: {materias_unidas}")


materias_comun = materias_juan.intersection(materias_ana).intersection(materias_pedro)
print(f"Estas son las materias en comun que tienen todos: {materias_comun}")

