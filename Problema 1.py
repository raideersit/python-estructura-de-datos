#Algoritmo con matrices
#Problema 1(Laboratorio 1(21/04/2023))

# crea un algoritmo donde se solicita dos matrices
# se pide la cantidad de columnas , como de filas
# los elementos generados deben ser ordenandos de manera aleatoria
# estas dos matrices se deben sumar
# Se solicita una tercera matriz, igualmente se solicitan columnas y filas
# Sus elementos deben ser generados de manera aleatoria (0 a 5)
# esta ultima matriz se resta con la matriz que se suma con la primera

import random

#Se solicitan datos de la primera matriz
filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))

#Generar la primera matriz con orden aleatorios
matriz1 = random.randint(0, 6, size=(filas1, columnas1))

#Solicitar el tamaño de la segunda matriz
filas2 = int(input("Por favor ,ingrese el número de filas de la segunda matriz: "))
columnas2 = int(input("Por favor, ingrese el número de columnas de la segunda matriz: "))

# Generar la segunda matriz con elementos aleatorios
matriz2 = random.randint(0, 6, size=(filas2, columnas2))

#Suma las matrices
matriz_suma = matriz1 + matriz2

#Solicita el tamaño de la tercera matriz
filas3 = int(input("Ingrese el número de filas de la tercera matriz: "))
columnas3 = int(input("Ingrese el número de columnas de la tercera matriz: "))

#Genera la tercera matriz con numeros aleatorios
matriz3 = random.randint(0, 6, size=(filas3, columnas3))

#Restar la tercera matriz a la matriz resultante de la suma
matriz_resultante = matriz_suma - matriz3

#se imprimen los resultados
print("Matriz 1:\n", matriz1)
print("Matriz 2:\n", matriz2)
print("Matriz Suma:\n", matriz_suma)
print("Matriz 3:\n", matriz3)
print("Matriz Resultante:\n", matriz_resultante)
