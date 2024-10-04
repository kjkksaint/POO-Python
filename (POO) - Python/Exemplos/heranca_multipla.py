class Ave:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(f"{self.nome} está voando.")

class Pinguim(Ave):
    def voar(self):  # Sobrescrevendo o método voar
        print(f"{self.nome} não pode voar, mas pode nadar!")

class Peixe:
    def __init__(self, nome):
        self.nome = nome

    def nadar(self):
        print(f"{self.nome} está nadando.")

# Herança múltipla: uma classe pode herdar características de mais de uma classe
class PinguimPeixe(Pinguim, Peixe):
    def __init__(self, nome):
        Pinguim.__init__(self, nome)
        Peixe.__init__(self, nome)

    def atividades(self):
        self.nadar()  # Chamando método da classe Peixe
        self.voar()   # Chamando método da classe Pinguim

# Criando objeto com herança múltipla
animal = PinguimPeixe("Pingu")
animal.atividades()

### EXPLICACAO:
# A classe PinguimPeixe herda tanto de Pinguim quanto de Peixe. Isso permite que a classe tenha métodos e atributos de ambas as classes.
# A herança múltipla pode ser usada para combinar comportamentos de diferentes classes em uma única classe.