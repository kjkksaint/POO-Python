# Definição de uma classe
class Carro:
        # Construtor: define os atributos do objeto
        def __init__(self, marca, modelo, ano):
           self.marca = marca
           self.modelo = modelo
           self.ano =  ano
           
        # Método para descrever o carro
        def descricao(self):
            return f"{self.ano} {self.marca} {self.modelo}"
        
# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Acessando o método
print(meu_carro.descricao())

# EXPLICAÇÃO: 

# __init__ é o construtor, chamado automaticamente ao criar um objeto da classe. Ele inicializa os atributos do objeto.
# descricao é um método da classe que retorna uma descrição do carro.