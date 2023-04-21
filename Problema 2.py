#Multiplicacion  de matriz por escalar ingresado
#Pregunta 2(Laboratorio 1(21/04/2023))


#Se solicita por teclado la cantidad de filas
#Tambien ingresar por consola un escalar
#Los elementos de la matriz deben ser generados aleatoriamente
#Desde el 0 al 10
#Se debe multiplicar la matriz generada por el escalar ingresado

import random


filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

#Se pìde escalar para multiplicar
escalar = int(input("Ingrese un escalar para multiplicar la matriz: "))

#Se defime la matriz
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(0, 10))
    matriz.append(fila)
#Se muestra la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)
#Multiplica la matriz por el escalar
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] *= escalar

print("\nMatriz obtenida:")
for fila in matriz:
    print(fila)





