# Programación Tradicional
# Ejemplo: Promedio semanal de temperatura

# Definición de variables globales
temperaturas = [0, 0, 0, 0, 0, 0, 0]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
total_temperatura = 0
promedio = 0

# Función para registrar temperaturas diarias
def registrar_temperaturas():
    global temperaturas
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dias_semana[i]}: "))
                temperaturas[i] = temp
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

# Función para calcular el promedio semanal
def calcular_promedio():
    global total_temperatura, promedio, temperaturas
    total_temperatura = sum(temperaturas)
    promedio = total_temperatura / len(temperaturas)

# Uso de las funciones en la programación tradicional
registrar_temperaturas()
calcular_promedio()

# Imprimir los resultados
print("Temperaturas registradas:", temperaturas)
print("Promedio semanal de temperatura:", round(promedio, 2), "°C")
