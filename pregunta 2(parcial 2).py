# SE NECESITA CREAR UN SISTEMA DE GESTION DE TAREAS
# UTILIZANDO LISTA BIDIRECCIONALES , CADA TAREA TIENE
# UN IDENTIFICADOR UNICO, UN TITULO, UNA DESCRIPCION 
# Y ESTADO(PENDIENTE, EN PROGRESO, O COMPLETADA)
# DEBE REALIZAR LAS SIGUIENTES TAREAS
# PERMITIR AGREGAR TAREAR
# ELIMINAR TAREAS
# BUSCAR UNA TAREA EN ESPECIFICO CAMBIAR EL ESTADO DE LAS TAREAS 
# MOSTRAR LAS TAREAS EN ORDEN ASCENDENTE SEGUN SU INDENTIFICADOR
class NodoTarea:
    def __init__(self, id, titulo, descripcion, estado):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.siguiente = None
        self.anterior = None

class SistemaGestionTareas:
    def __init__(self):
        self.primera_tarea = None
        self.ultima_tarea = None

    def agregar_tarea(self, id, titulo, descripcion, estado):
        nueva_tarea = NodoTarea(id, titulo, descripcion, estado)

        if self.primera_tarea is None:
            self.primera_tarea = nueva_tarea
            self.ultima_tarea = nueva_tarea
        else:
            nueva_tarea.anterior = self.ultima_tarea
            self.ultima_tarea.siguiente = nueva_tarea
            self.ultima_tarea = nueva_tarea

    def eliminar_tarea(self, id):
        tarea_actual = self.primera_tarea

        while tarea_actual is not None:
            if tarea_actual.id == id:
                if tarea_actual.anterior is not None:
                    tarea_actual.anterior.siguiente = tarea_actual.siguiente
                else:
                    self.primera_tarea = tarea_actual.siguiente

                if tarea_actual.siguiente is not None:
                    tarea_actual.siguiente.anterior = tarea_actual.anterior
                else:
                    self.ultima_tarea = tarea_actual.anterior

                del tarea_actual
                return

            tarea_actual = tarea_actual.siguiente

    def buscar_tarea(self, id):
        tarea_actual = self.primera_tarea

        while tarea_actual is not None:
            if tarea_actual.id == id:
                return tarea_actual

            tarea_actual = tarea_actual.siguiente

        return None       
          
    def actualizar_estado(self, id, nuevo_estado):
        tarea = self.buscar_tarea(id)

        if tarea is not None:
            tarea.estado = nuevo_estado

    def actualizar_estado(self, id, nuevo_estado):
        tarea = self.buscar_tarea(id)

        if tarea is not None:
            tarea.estado = nuevo_estado

    def mostrar_tareas(self):
        tarea_actual = self.primera_tarea

        while tarea_actual is not None:
            print("ID:", tarea_actual.id)
            print("Titulo:", tarea_actual.titulo)
            print("Descripcion:", tarea_actual.descripcion)
            print("Estado:", tarea_actual.estado)
            print()
            tarea_actual = tarea_actual.siguiente
