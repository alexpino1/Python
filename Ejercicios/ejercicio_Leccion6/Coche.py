class Vehiculo:
    color="Rojo"
    Ruedas=4
    Puertas=4

class Coche(Vehiculo):
    Velocidad=120
    Cilindraje=1600

coche=Coche()
print("Caracteristicas\n"
      "color: ",coche.color,"\n",
      "velocidad: ",coche.Velocidad,"\n",
      "Cilindraje: ",coche.Cilindraje,"\n",
      "Numero de puertas: ",coche.Puertas,"\n",
      "Cantidad de ruedas: ",coche.Ruedas)