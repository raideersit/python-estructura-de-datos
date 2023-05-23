import random

dimension = random.randint(3, 5)
matriz = []
for i in range(dimension):
    fila = [random.randint(1, 10) for _ in range(dimension)]
    matriz.append(fila)
for i in range(dimension):
    for j in range(dimension):
        if i == j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)
for i in range(dimension):
    # Dividir la fila i por el elemento diagonal
    diagonal = matriz[i][i]
    for j in range(dimension * 2):
        matriz[i][j] /= diagonal

    # Restar la fila i de las demás filas para obtener ceros en las columnas por debajo de la diagonal
    for k in range(dimension):
        if k != i:
            factor = matriz[k][i]
            for j in range(dimension * 2):
                matriz[k][j] -= factor * matriz[i][j]
matriz_inversa = []
for i in range(dimension):
    fila_inversa = matriz[i][dimension:]
    matriz_inversa.append(fila_inversa)
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz inversa:")
for fila in matriz_inversa:
    print(fila)
