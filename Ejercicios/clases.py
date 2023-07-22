#CLASES ESTATICAS
# COMPARTE EL MISMO ESPACIO DE MEMORIA

class Estatica:
    numero=1

    def incremento(self):
        Estatica.numero+=1

#LAS CLASES DINAMICAS TIENEN DIFERENTE ESPACIO DE MEMORIA

class Dinamica:
    _encendido = True

    def apaga(self):
        self._encendido= False
    def isEncendido(self):
        self._encendido= True
    def enciende(self):
        self._encendido= True
#HERENCIA

class Miclase(Dinamica): # de esta mande se heresa elementos de clase dinamica
   pass


