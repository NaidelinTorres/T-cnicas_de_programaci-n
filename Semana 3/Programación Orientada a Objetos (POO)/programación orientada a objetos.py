# Programación Orientada a Objetos (POO)
# Ejemplo: Promedio semanal de temperatura

class SemanaClimatica:
    def __init__(self):
        self.temperaturas = [0] * 7
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def registrar_temperaturas(self):
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {self.dias_semana[i]}: "))
                    self.temperaturas[i] = temp
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Crear una instancia de la clase SemanaClimatica
semana = SemanaClimatica()

# Uso de los métodos en POO
semana.registrar_temperaturas()
promedio = semana.calcular_promedio()

# Imprimir resultados
print("Temperaturas registradas:", semana.temperaturas)
print(f"Promedio semanal de temperatura: {promedio:.2f} °C")
