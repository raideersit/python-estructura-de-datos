# Crear la matriz
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        elemento = int(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
        fila.append(elemento)
    matriz.append(fila)

# Calcular la suma de cada columna
sumas_columnas = []
for j in range(5):
    suma_columna = sum(matriz[i][j] for i in range(5))
    sumas_columnas.append(suma_columna)

# Encontrar la suma más alta entre las columnas
suma_mas_alta = max(sumas_columnas)

# Calcular la suma de cada fila
sumas_filas = []
for i in range(5):
    suma_fila = sum(matriz[i])
    sumas_filas.append(suma_fila)

# Encontrar la suma más baja entre las filas
suma_mas_baja = min(sumas_filas)

# Imprimir los resultados
print("Matriz:")
for fila in matriz:
    print(fila)

print("Suma más alta entre las columnas:", suma_mas_alta)
print("Suma más baja entre las filas:", suma_mas_baja)
