# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias_semana:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                # Validar rango de temperatura opcionalmente
                if -50 <= temp <= 60:
                    temperaturas.append(temp)
                    break
                else:
                    print("Temperatura fuera de rango (-50 a 60 °C). Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Cálculo del promedio semanal del clima")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
