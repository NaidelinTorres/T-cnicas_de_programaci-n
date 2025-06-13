class Vehiculo:
    def mostrar_info(self):
        print("Información general del vehículo.")

class Auto(Vehiculo):
    def mostrar_info(self):
        print("Auto: vehículo, ideal para la ciudad.")

class Moto(Vehiculo):
    def mostrar_info(self):
        print("Moto: vehículo, ágil y compacto.")

class Bicicleta(Vehiculo):
    def mostrar_info(self):
        print("Bicicleta: vehículo sin motor, ecológico y saludable.")

# Uso del polimorfismo
vehiculos = [Vehiculo(), Auto(), Moto(), Bicicleta()]

for v in vehiculos:
    v.mostrar_info()

