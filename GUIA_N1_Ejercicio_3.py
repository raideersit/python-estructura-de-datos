import numpy as np

# Generar una matriz de 3x3 con elementos aleatorios
matriz = np.random.rand(3, 3)

# Calcular la determinante de la matriz
determinante = np.linalg.det(matriz)

# Imprimir la matriz y su determinante
print("Matriz:")
print(matriz)
print("Determinante:", determinante)