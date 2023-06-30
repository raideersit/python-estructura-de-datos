# DESARROLLAR UNA SOLUCION PARA UNA APLICACION DE REPRODUCCION
# UTILIZANDO UNA LISTA CIRCULAR SIMPLE PARA ADMINISTRAR 
# LA LISTA DE VIDEO DE CADA USUARIO EN ESPECIFICO. CADA VIDEO
# TIENE UN TITULO, UN AUTOR Y UNA DURACION. SE SOLICITA IMPLEMENTAR 
# UNA LISTA ENLAZADA PARA UNA LISTA DE REPRODUCCION DE VIDEOS. DEBE 
# CONTENER LAS SIGUIENTES FUNCIONES
# CLASES RESPECTIVAS DEL PROBLEMA
# METODO PARA AGREGAR VIDEOS
# METODO PARA MOSTRAR LA LISTA DE VIDEOS
# METODO PARA BUSCAR VIDEOS
# METODO PARA ELIMINAR UN VIDEOS
# MEOTODO PAR VERIFICAR SI LA LISTA DE VIDEOS ESTA VACIA



def esta_vacia(self):
    return self.cabeza 

def agregar_video(self, video):
    nuevo_nodo = Nodo(video)
    if self.esta_vacia():
        nuevo_nodo.siguiente = nuevo_nodo
        self.cabeza = nuevo_nodo
    else:
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = self.cabeza

def mostrar_videos(self):
    if self.esta_vacia():
        print("esta vacia la lista de videos.")
        return
    actual = self.cabeza
    while True:
        print("titulo:", actual.video.titulo)
        print("Autor:", actual.video.autor)
        print("Duracion:", actual.video.duracion)
        print()
        actual = actual.siguiente
        if actual == self.cabeza:
            break

def buscar_video(self, titulo):
    if self.esta_vacia():
        print("esta vacia la lista.")
        return None
    actual = self.cabeza
    while True:
        if actual.video.titulo == titulo:
            return actual.video
        actual = actual.siguiente
        if actual == self.cabeza:
            break
    print("no se ha encontrado el video.")
    return None

def eliminar_video(self, titulo):
    if self.esta_vacia():
        print("no hay videos en la lista.")
        return
    if self.cabeza.video.titulo == titulo:
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        print("se ha eliminado el video.")
        return
    actual = self.cabeza
    anterior = None
    while True:
        if actual.video.titulo == titulo:
            anterior.siguiente = actual.siguiente
            print("El video ha sido eliminado.")
            return
        anterior = actual
        actual = actual.siguiente
        if actual == self.cabeza:
            break
    print("no se ha encontrado el video.")