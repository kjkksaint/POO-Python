class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f"{self.nome} está fazendo um som.")
        
class Cachorro(Animal): # A classe Cachorro herda de Animal
    def emitir_som(self): # Sobrescreve o método emitir_som
        print(f"{self.nome} está latindo.")
        
class Gato(Animal): # A classe Gato herda de Animal
    def emitir_som(self) # Sobrescreve o método emitir_som
        print(f"{self.nome} está miando.")
        
# Usando herança e polimorfismo
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

cachorro.emitir_som()
gato.emitir_som()

# Explicação:

# Cachorro e Gato são subclasses de Animal. Elas herdam os atributos e métodos da classe Animal.
# A função emitir_som é sobrescrita nas subclasses para comportamentos específicos.