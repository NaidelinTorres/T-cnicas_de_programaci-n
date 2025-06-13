class Pelicula:
    def mostrar_info(self):
        print("Información general de la película.")

class PeliculaFisica(Pelicula):
    def mostrar_info(self):
        print("Película física: se entrega en DVD.")

class PeliculaDigital(Pelicula):
    def mostrar_info(self):
        print("Película digital: se descarga en línea.")

# Uso del polimorfismo
peliculas = [Pelicula(), PeliculaFisica(), PeliculaDigital()]

for pelicula in peliculas:
    pelicula.mostrar_info()
