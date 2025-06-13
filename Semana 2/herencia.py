class Pelicula:
    def __init__(self, nombre, autor, precio):
        self.nombre = nombre
        self.autor = autor
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.nombre} de {self.autor}, Precio: ${self.precio}")

class PeliculaDigital(Pelicula):
    def __init__(self, nombre, autor, precio, formato):
        super().__init__(nombre, autor, precio)
        self.formato = formato

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato: {self.formato}")

# Aquí se usa la clase (esta parte es la que ejecuta)
mi_pelicula = PeliculaDigital("Camino hacia el terror", "Alan B. McElroy", 12.99, "MP4")
mi_pelicula.mostrar_info()
