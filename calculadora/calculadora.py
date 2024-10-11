class Calculadora:
    """Classe que implementa operações matemáticas básicas com validação de entradas."""

    def adicionar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("As entradas devem ser números.")
        return a + b

    def subtrair(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("As entradas devem ser números.")
        return a - b

    def multiplicar(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("As entradas devem ser números.")
        return a * b

    def dividir(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("As entradas devem ser números.")
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def fatorial(self, n):
        if not isinstance(n, int):
            raise TypeError("A entrada deve ser um número inteiro.")
        if n < 0:
            raise ValueError("Fatorial de número negativo não é permitido.")
        return 1 if n == 0 else n * self.fatorial(n - 1)

    def potencia(self, base, expoente):
        if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
            raise TypeError("As entradas devem ser números.")
        return base ** expoente
