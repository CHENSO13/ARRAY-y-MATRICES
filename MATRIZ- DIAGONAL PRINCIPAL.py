#la funcion numpy calcula la diagonal principal de una matriz.
import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # matriz de 3x3
diagonal = np.diag(matriz)
print(diagonal)
