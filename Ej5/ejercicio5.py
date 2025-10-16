#Crear un diccionario donde la clave sea el departamento y el valor sea la suma de edades de los empleados de ese departamento.

#Imprimir solo los departamentos donde la edad total sea mayor a 25.

#Agregar un nuevo empleado.

empleados = [
    {"nombre": "Ana", "edad": 25, "departamento": "Ventas"},
    {"nombre": "Luis", "edad": 30, "departamento": "Ventas"},
    {"nombre": "Maria", "edad": 18, "departamento": "RRHH"},
    {"nombre": "Pepe", "edad": 25, "departamento": "Ventas"},
    {"nombre": "Javier", "edad": 26, "departamento": "Marketing"}
]

lista_departamentos =[]
lista_departamentos_edad = []

for empleado in empleados:
    lista_general = []
    for key,value in empleado.items():
        if key == "departamento":
            lista_departamentos.append(value)
            lista_general.append(value)
        if key == "edad":
            lista_general.append(value)
    lista_departamentos_edad.append(lista_general)

diccionario_departamentos = dict.fromkeys(lista_departamentos,0)

for edad,departamento in lista_departamentos_edad:
    diccionario_departamentos[departamento] += edad
print(f"Diccionario con departamento y la suma de edades de empleados: {diccionario_departamentos}\n")

print("Departamentos con empleados con edad mayor a 25 años")
for departamento, edad in diccionario_departamentos.items():
    if edad >= 25:
        print(departamento,edad)
print()

print("Nuevo empleado")
for empleado in empleados:
    lista_claves = list(empleado.keys())

dic_nuevo_empleado = {}
for clave in lista_claves:
    if clave == "nombre" or clave == "departamento":
        valor = input(f"Ingresa {clave} del empleado: ")
    else:
        valor =int(input(f"Ingresa {clave} del empleado: "))
    dic_nuevo_empleado.setdefault(clave,valor)

empleados.append(dic_nuevo_empleado)

print(f"Empleado agregado con exito")

for empleado in empleados:
    print(empleado)







    
    




    


       


