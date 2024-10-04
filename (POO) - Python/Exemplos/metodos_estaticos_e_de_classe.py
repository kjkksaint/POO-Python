class Calculadora:
    @staticmethod
    def somar(a, b)
        return a + b
    
    @classmethod
    def criar_instancia(cls):
        return cls()
    
# chamando métodos estáticos e de classe
print(Calculadora.somar(5, 10)) # Não precisa de uma intância para ser chamado

calculadora = Calculadora.criar_instancia() # Cria uma instância da classe usando o método de classe

## EXPLICACAO

# somar é um método estático porque não precisa de uma instância para ser chamado.
# criar_instancia é um método de classe e retorna uma nova instância da própria classe.