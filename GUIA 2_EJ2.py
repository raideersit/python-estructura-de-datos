class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return not bool(self.elementos)

    def agregar(self, dato):
        self.elementos.append(dato)

    def eliminar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("La cola está vacía")

    def tamano(self):
        return len(self.elementos)


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numero_ticket = None
        self.numero_caja = None


class Farmacia:
    def __init__(self):
        self.cola = Cola()
        self.clientes = {}

    def agregar_cliente(self, nombre):
        cliente = Cliente(nombre)
        numero_ticket = len(self.clientes) + 1
        cliente.numero_ticket = numero_ticket
        self.clientes[numero_ticket] = cliente
        self.cola.agregar(numero_ticket)

    def procesar_cliente(self):
        if not self.cola.esta_vacia():
            numero_ticket = self.cola.eliminar()
            cliente = self.clientes[numero_ticket]
            if not cliente.numero_caja:
                if numero_ticket % 3 == 1:
                    cliente.numero_caja = 1
                elif numero_ticket % 3 == 2:
                    cliente.numero_caja = 2
                else:
                    cliente.numero_caja = 3

            print(f"Cliente {cliente.nombre} se dirige a la caja {cliente.numero_caja}")
        else:
            print("No hay clientes en la cola")

