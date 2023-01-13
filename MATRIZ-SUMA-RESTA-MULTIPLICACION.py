#suma de matriz

#amabas matrices deben tener las mismas dimensiones

def suma(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Ejemplo de uso
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = suma(A, B)

if result == None:
    print("No se puede sumar")
else:
    for fila in result:
        print("[", end=" ")
        for elemento in fila:
            print(elemento,end=" ")
        print("]")


#%%

# resta de matriz

def resta(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] - B[i][j]
    return C

# Ejemplo de uso
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = resta(A, B)

if resultado == None:
    print("No se puede sumar")
else:
    for fila in resultado:
        print("[", end=" ")
        for elemento in fila:
            print(elemento,end=" ")
        print("]")

#%%
# multiplicacion de matrices


def multiplicacion(A, B):
    filaA = len(A)
    columnaA = len(A[0])
    filaB = len(B)
    columnaB = len(B[0])

    if columnaA != filaB:
        raise ValueError("Las dimensiones de las matrices no son válidas para la multiplicación")

    C = [[0 for j in range(columnaB)] for i in range(filaA)]
    for i in range(filaA):
        for j in range(columnaB):
            for k in range(columnaA):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Ejemplo de uso
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
resultadoo = multiplicacion(A, B)

if resultadoo == None:
    print("No se puede sumar")
else:
    for fila in resultado:
        print("[", end=" ")
        for elemento in fila:
            print(elemento,end=" ")
        print("]")