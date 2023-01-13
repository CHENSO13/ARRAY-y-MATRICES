#determinante de una matriz
# solo funciona para matrices cuadradas

import numpy as np

A = np.array([[11, 11, 11], [14, 4, 44], [48, 78, 89]])
determinante = np.linalg.det(A)
print(determinante)

