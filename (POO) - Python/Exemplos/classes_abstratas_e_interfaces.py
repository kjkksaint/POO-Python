from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass  # Este método deve ser implementado pelas subclasses

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

# Usando classes abstratas
formas = [Retangulo(10, 20), Circulo(5)]

for forma in formas:
    print(f"A área da forma é: {forma.calcular_area()}")


### Explicação:
# FormaGeometrica é uma classe abstrata. Não pode ser instanciada diretamente, apenas subclasses podem ser criadas.
# @abstractmethod indica que o método deve ser implementado em qualquer classe derivada.