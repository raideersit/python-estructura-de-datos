class Almacen:
    def __init__(self):
        self.productos_recibidos = []
        self.productos_a_despachar = []

    def agregar_producto(self, producto):
        self.productos_recibidos.append(producto)
        print(f"Producto '{producto}' agregado al almacén.")



    def despachar_producto(self):
        if not self.productos_a_despachar:
            print("No hay productos disponibles para despachar.")
        else:
            producto = self.productos_a_despachar.pop(0)
            print(f"Producto '{producto}' despachado.")



    def verificar_vacio(self, lista, nombre_lista):
        if not lista:
            print(f"La {nombre_lista} está vacía.")
        else:
            print(f"La {nombre_lista} no está vacía.")



    def imprimir_lista(self, lista, nombre_lista):
        print(f"Lista de {nombre_lista}:")
        for producto in lista:
            print(producto)



    def mostrar_cantidad_total_productos(self):
        cantidad_total = len(self.productos_recibidos) + len(self.productos_a_despachar)
        print(f"Cantidad total de productos en el almacén: {cantidad_total}")



