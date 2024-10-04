class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # Atributo privado, começa com dois underline ( __ )
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if valor <= self.__saldo
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")
            
    def mostrar_saldo(self):
        return f"Saldo de {self.titular}: {self.__saldo}"
    
# Usando a classe ContaBancaria
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
print(conta.mostra_saldo())

# Explicação

# O atributo __saldo é privado, o que significa que não pode ser acessado diretamente fora da classe.

# Métodos como depositar, sacar e mostrar_saldo controlam o acesso a __saldo.