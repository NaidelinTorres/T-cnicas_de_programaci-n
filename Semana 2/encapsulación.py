class Pelicula:
    def __init__(self, nombre, autor, precio):
        self.__nombre = nombre      # atributos privados
        self.__autor = autor
        self.__precio = precio
        self.__disponible = True

    def comprar(self):
        if self.__disponible:
            print(f"Has comprado la película: {self.__nombre}")
            self.__disponible = False
        else:
            print(f"La película {self.__nombre} ya fue comprada.")

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Autor: {self.__autor}")
        print(f"Precio: {self.__precio} USD")
        print("Disponible:", "Sí" if self.__disponible else "No")


# Aquí comienza el uso de la clase
mi_pelicula = Pelicula("Camino hacia el terror", "Alan B. McElroy", 12.99)

mi_pelicula.mostrar_info()
mi_pelicula.comprar()
mi_pelicula.mostrar_info()
