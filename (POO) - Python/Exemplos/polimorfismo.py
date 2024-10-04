class Forma:
    def area(self):
        pass # Classe abstrata, não implementação
    
class Retangulo(forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return 3.14 * (self.raio ** 2)
    
  ### Usando polimorfismo
 formas = [retangulo(10,20), Circulo(5)]
 
 for forma in formas:
     print(f"A área da forma é: {forma.area()}")
     
### EXPLICAÇÃO:

# Forma é uma classe base abstrata.
# Retangulo e Circulo implementam o método area de maneira diferente.
# O polimorfismo nos permite tratar objetos de diferentes classes de maneira unificada.