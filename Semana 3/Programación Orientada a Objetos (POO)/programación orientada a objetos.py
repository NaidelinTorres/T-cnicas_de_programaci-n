class SemanaClimatica:
    def __init__(self):
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = [0.0] * 7

    def registrar_temperaturas(self):
        for i, dia in enumerate(self.dias_semana):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    if -50 <= temp <= 60:
                        self.temperaturas[i] = temp
                        break
                    else:
                        print("Temperatura fuera de rango (-50 a 60 °C). Intente de nuevo.")
                except ValueError:
                    print("Por favor, ingrese un valor numérico válido.")

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resumen(self):
        print("\nTemperaturas registradas por día:")
        for dia, temp in zip(self.dias_semana, self.temperaturas):
            print(f"{dia}: {temp} °C")
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal de temperatura: {promedio:.2f} °C")

def main():
    print("Cálculo del promedio semanal del clima (POO)")
    semana = SemanaClimatica()
    semana.registrar_temperaturas()
    semana.mostrar_resumen()

if __name__ == "__main__":
    main()
