class Alumno:
    def __init__(self, Nombre, Nota):
        self.Nombre = Nombre
        self.Nota = Nota

    def Datos_alumnos(self):
        super.Nombre = ""
        super.Nota = 0

    def Resultado(self):
        if self.Nota >= 3.5:
            print("El alumno ", self.Nombre, "Con la Nota: ", self.Nota, "Aprobo")
        else:
            print("El alumno ", self.Nombre, "Con la Nota: ", self.Nota, "Reprobo")


Alumno1 = Alumno("Miguel", 3.5)
Alumno1.Resultado()
Alumno2 = Alumno("Sara", 3)
Alumno2.Resultado()
Alumno3 = Alumno("Sebas", 4)
Alumno3.Resultado()