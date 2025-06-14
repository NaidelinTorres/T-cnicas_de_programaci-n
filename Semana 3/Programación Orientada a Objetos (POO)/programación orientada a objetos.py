class SemanaClimatica:
    def __init__(self):
        self.temperaturas = [0] * 7
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def registrar_temperaturas(self):
        for indice, dia in enumerate(self.dias_semana):  # 'indice' es int
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    if -50 <= temp <= 60:
                        self.temperaturas[indice] = temp  # uso correcto de índice
                        break
                    else:
                        print("Temperatura fuera de rango (-50 a 60 °C). Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resumen(self):
        print("\nTemperaturas registradas:")
        for dia, temp in zip(self.dias_semana, self.temperaturas):
            print(f"{dia}: {temp} °C")
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal de temperatura: {promedio:.2f} °C")

# Ejecución
semana = SemanaClimatica()
semana.registrar_temperaturas()
semana.mostrar_resumen()
