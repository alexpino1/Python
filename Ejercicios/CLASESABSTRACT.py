from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class perro(Animal):
    def sonido(self):
        print("guao guao ")

p = perro()
p.sonido()
