#Ejemplo de abstraccion
class Pelicula:
    def __init__(self, nombre, autor, precio):
        self.nombre = nombre
        self.autor = autor
        self.precio = precio
        self.__disponible = True  # detalle interno oculto

    def comprar(self):
        if self.__disponible:
            print(f"Has comprado la película: {self.nombre}")
            self.__disponible = False
        else:
            print(f"La película {self.nombre} ya fue comprada.")

# Usuario interactúa solo con comprar(), no sabe cómo se maneja la disponibilidad interna
mi_pelicula = Pelicula("Camino hacia el terror", "Alan B. McElroy", "12.99")
mi_pelicula.comprar()
mi_pelicula.comprar()

