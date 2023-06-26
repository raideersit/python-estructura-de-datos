class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_song(self, titulo, artista):
        nueva_cancion = Cancion(titulo, artista)
        if self.is_empty():
            self.head = nueva_cancion
            self.tail = nueva_cancion
        else:
            nueva_cancion.prev = self.tail
            self.tail.next = nueva_cancion
            self.tail = nueva_cancion

    def remove_song(self, titulo):
        current_song = self.head
        while current_song:
            if current_song.titulo == titulo:
                if current_song.prev:
                    current_song.prev.next = current_song.next
                else:
                    self.head = current_song.next

                if current_song.next:
                    current_song.next.prev = current_song.prev
                else:
                    self.tail = current_song.prev

                break
            current_song = current_song.next

    def display_playlist(self):
        current_song = self.head
        while current_song:
            print(f"Titulo: {current_song.titulo}, Artista: {current_song.artista}")
            current_song = current_song.next


# Crear una nueva lista de reproducción
my_playlist = Playlist()

# Agregar canciones a la lista de reproducción
my_playlist.add_song("Cancion 1", "Artista 1")
my_playlist.add_song("Cancion 2", "Artista 2")
my_playlist.add_song("Cancion 3", "Artista 3")

# Mostrar la lista de reproducción
my_playlist.display_playlist()

# Eliminar una canción de la lista de reproducción
my_playlist.remove_song("Cancion 2")

# Mostrar la lista de reproducción actualizada
my_playlist.display_playlist()
