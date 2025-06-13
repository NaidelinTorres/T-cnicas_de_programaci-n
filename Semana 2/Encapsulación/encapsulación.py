#Ejemplo de encapsulacion
class Musica:
    def __init__(self, nombre, artista, precio):
        self.__nombre = nombre      # atributos privados
        self.__artista = artista
        self.__precio = precio
        self.__disponible = True

    def comprar(self):
        if self.__disponible:
            print(f"Has comprado la canción: {self.__nombre}")
            self.__disponible = False
        else:
            print(f"La canción {self.__nombre} ya fue comprada.")

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Artista: {self.__artista}")
        print(f"Precio: {self.__precio} USD")
        print("Disponible:", "Sí" if self.__disponible else "No")


# Uso de la clase
mi_cancion = Musica("Havana", "Camila Cabello", 10.50)

mi_cancion.mostrar_info()
mi_cancion.comprar()
mi_cancion.mostrar_info()
