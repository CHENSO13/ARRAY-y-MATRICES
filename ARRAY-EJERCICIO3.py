array = []
tamaño = int(input("Defina el tamaño del Array:"))
funcion = int(input("Ingrese un numero: "))
array.append(funcion)
for n in range(tamaño-1):
    funcion = 2*funcion #aqui creamos cualquier funcion 
    array.append(funcion)
print(array)