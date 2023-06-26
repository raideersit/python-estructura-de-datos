class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.subordinados = []

class JerarquiaEmpresa:
    def __init__(self):
        self.raiz = None

    def agregar_empleado(self, nombre, cargo, jefe_directo=None):
        empleado = Empleado(nombre, cargo)
        if jefe_directo is None:
            self.raiz = empleado
        else:
            jefe_directo.subordinados.append(empleado)

    def eliminar_empleado(self, nombre):
        if self.raiz is None:
            return
        if self.raiz.nombre == nombre:
            self.raiz = None
            return
        self._eliminar_empleado_recursivo(self.raiz, nombre)

    def _eliminar_empleado_recursivo(self, empleado, nombre):
        for subordinado in empleado.subordinados:
            if subordinado.nombre == nombre:
                empleado.subordinados.remove(subordinado)
                return
            self._eliminar_empleado_recursivo(subordinado, nombre)

    def mostrar_jerarquia(self):
        if self.raiz is None:
            print("La jerarquía está vacía")
            return
        self._mostrar_jerarquia_recursivo(self.raiz, 0)

    def _mostrar_jerarquia_recursivo(self, empleado, nivel):
        print("  " * nivel + empleado.nombre + " - " + empleado.cargo)
        for subordinado in empleado.subordinados:
            self._mostrar_jerarquia_recursivo(subordinado, nivel + 1)

    def buscar_empleado(self, nombre):
        if self.raiz is None:
            print("La jerarquía está vacía")
            return
        empleado = self._buscar_empleado_recursivo(self.raiz, nombre)
        if empleado:
            print("Nombre:", empleado.nombre)
            print("Cargo:", empleado.cargo)
            if empleado.subordinados:
                print("Subordinados directos:")
                for subordinado in empleado.subordinados:
                    print(subordinado.nombre + " - " + subordinado.cargo)
        else:
            print("Empleado no encontrado")

    def _buscar_empleado_recursivo(self, empleado, nombre):
        if empleado.nombre == nombre:
            return empleado
        for subordinado in empleado.subordinados:
            resultado = self._buscar_empleado_recursivo(subordinado, nombre)
            if resultado:
                return resultado
        return None

    def obtener_jefe_directo(self, nombre):
        if self.raiz is None:
            print("La jerarquía está vacía")
            return
        empleado = self._obtener_jefe_directo_recursivo(self.raiz, nombre)
        if empleado:
            print("Jefe directo:")
            print("Nombre:", empleado.nombre)
            print("Cargo:", empleado.cargo)
        else:
            print("Empleado no encontrado")

    def _obtener_jefe_directo_recursivo(self, empleado, nombre):
        for subordinado in empleado.subordinados:
            if subordinado.nombre == nombre:
                return empleado
            resultado = self._obtener_jefe_directo_recursivo(subordinado, nombre)
            if resultado:
                return resultado
        return None


# Ejemplo de uso del programa

# Crear una nueva jerarquía de empresa
jerarquia = JerarquiaEmpresa()

# Agregar empleados a la jerarquía
jerarquia.agregar_empleado("Juan", "CEO")
jerarquia.agregar_empleado("María", "Directora", jerarquia.raiz)
jerarquia.agregar_empleado("Pedro", "Gerente", jerarquia.raiz)
jerarquia.agregar_empleado("Ana", "Supervisora", jerarquia.raiz.subordinados[1])
jerarquia.agregar_empleado("Luis", "Analista", jerarquia.raiz.subordinados[1].subordinados[0])

# Mostrar la jerarquía completa
jerarquia.mostrar_jerarquia()


# Buscar un empleado en la jerarquía
jerarquia.buscar_empleado("Pedro")


# Obtener el jefe directo de un empleado
jerarquia.obtener_jefe_directo("Ana")


# Eliminar un empleado de la jerarquía
jerarquia.eliminar_empleado("Pedro")

# Mostrar la jerarquía después de la eliminación
jerarquia.mostrar_jerarquia()

