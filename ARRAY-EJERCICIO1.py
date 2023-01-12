nombre = []  #nombres
longitud = []  #longitud de los nombres
nombres = int(input("Ingrese el tamaño del array: "))
for nomb in range(nombres):
    nuevo = (input("Ingrese un nombre: "))
    nombre.append(nuevo)
    tamaño = len(nuevo)
    longitud.append(tamaño)

print(nombre)
print(longitud)
    

    