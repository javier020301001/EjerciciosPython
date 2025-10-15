#Contar cuántas veces 
# aparece una letra en varias palabras
#  y mostrar solo las 
# palabras que la contienen.


palabras = ["python", "programar", 
            "divertido", "logica", 
            "datos"]

print(palabras)
letra = input("Ingresa una letra para saber cuantas veces aparece: ")
sum = 0
lista_palabras = []

for palabra in palabras:
    if letra in palabra:
        sum += palabra.count(letra)
        lista_palabras.append(palabra)

if sum == 0:
    print("No se encontro la letra en la lista de palabras!!")
else:   
    print(f"La letra {letra} aparece un total: {sum}")
    print(f"Las palabras que contienen la letra {letra} son: {lista_palabras}")
