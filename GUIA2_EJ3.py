import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def calcular_media(self):
        if self.cabeza is None:
            return None
        suma = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma += nodo_actual.dato
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return suma / contador

    def calcular_desviacion_estandar(self):
        if self.cabeza is None:
            return None
        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma_cuadrados += (nodo_actual.dato - media) ** 2
            contador += 1
            nodo_actual = nodo_actual.siguiente
        varianza = suma_cuadrados / contador
        desviacion_estandar = math.sqrt(varianza)
        return desviacion_estandar

    def imprimir_lista(self):
        if self.cabeza is None:
            print("La lista está vacía")
            return
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def verificar_lista_vacia(self):
        return self.cabeza is None


# Crear una nueva lista enlazada
lista = ListaEnlazada()

# Ingresar los datos por teclado
num_datos = int(input("Ingrese el número de datos: "))
for _ in range(num_datos):
    dato = float(input("Ingrese un dato: "))
    lista.agregar_dato(dato)

# Imprimir la lista
lista.imprimir_lista()
# Output: Los datos ingresados por teclado

# Calcular la media
media = lista.calcular_media()
print("Media:", media)

# Calcular la desviación estándar
desviacion_estandar = lista.calcular_desviacion_estandar()
print("Desviación estándar:", desviacion_estandar)

# Verificar si la lista está vacía
vacia = lista.verificar_lista_vacia()
print("Lista vacía:", vacia)
