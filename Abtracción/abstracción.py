class Pelicula:
    def __init__(self, nombre, autor, precio):
        self.nombre = nombre
        self.autor = autor
        self.precio = precio
        self.__disponible = True

    def comprar(self):
        if self.__disponible:
            print(f"Has comprado la película: {self.nombre}")
            self.__disponible = False
        else:
            print(f"La película {self.nombre} ya fue comprada.")

    def esta_disponible(self):
        return self.__disponible


# Crear un objeto Pelicula
mi_pelicula = Pelicula("Camino hacia el terror", "Alan B. McElroy", "12,99")

# Usar el método comprar
mi_pelicula.comprar()
mi_pelicula.comprar()
