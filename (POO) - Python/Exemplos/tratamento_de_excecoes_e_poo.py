class Calculadora:
    def dividir(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Erro: Divisão por zero não permitida.")
            return None

# Usando a Calculadora
calc = Calculadora()
resultado = calc.dividir(10, 0)  # Tenta dividir por zero
print("Resultado:", resultado)

### Explicação: O tratamento de exceções (try/except) é uma maneira de capturar erros durante a execução do código e impedir que ele falhe de maneira descontrolada.