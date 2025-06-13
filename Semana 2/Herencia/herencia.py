class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.titulo} de {self.autor}, Precio: ${self.precio}")

class LibroDigital(Libro):
    def __init__(self, titulo, autor, precio, formato):
        super().__init__(titulo, autor, precio)
        self.formato = formato

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Formato: {self.formato}")

# Uso
mi_libro = LibroDigital("Crepúsculo", "Stephenie Meyer", 40.49, "PDF")
mi_libro.mostrar_info()
