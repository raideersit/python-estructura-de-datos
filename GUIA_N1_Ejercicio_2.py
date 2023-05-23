import numpy as np

# Definir una matriz A
A = np.array([[2, 1], [4, 3]])

# Calcular la matriz inversa de A
A_inv = np.linalg.inv(A)

# Calcular el producto A × A⁻¹
producto = np.dot(A, A_inv)

# Obtener la matriz identidad
identidad = np.eye(A.shape[0])

# Verificar si A × A⁻¹ es igual a la matriz identidad
if np.array_equal(producto, identidad):
    print("La propiedad A × A⁻¹ = I se cumple.")
else:
    print("La propiedad A × A⁻¹ = I no se cumple.")
