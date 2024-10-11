import pytest
from calculadora import Calculadora

# Fixture para instanciar a calculadora
@pytest.fixture
def calc():
    return Calculadora()

# Testes de operações básicas com números positivos e negativos
def test_adicionar(calc):
    assert calc.adicionar(1, 2) == 3
    assert calc.adicionar(-1, -2) == -3
    assert calc.adicionar(1e10, 1e10) == 2e10  

def test_subtrair(calc):
    assert calc.subtrair(5, 3) == 2
    assert calc.subtrair(-5, -3) == -2
    assert calc.subtrair(1e10, 1e9) == 9e9  

def test_multiplicar(calc):
    assert calc.multiplicar(3, 2) == 6
    assert calc.multiplicar(-3, -2) == 6
    assert calc.multiplicar(1e5, 1e5) == 1e10  

# Testar divisões que resultam em valores decimais e tratamento de divisão por zero
def test_dividir(calc):
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(9, 2) == 4.5
    assert calc.dividir(1e9, 1e3) == 1e6  
    with pytest.raises(ValueError):
        calc.dividir(10, 0)

# Testar fatorial com valores válidos e inválidos
def test_fatorial(calc):
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    with pytest.raises(ValueError):
        calc.fatorial(-5)  
    with pytest.raises(RecursionError):
        calc.fatorial(3000)  

# Testar a função de potência com expoentes positivos e negativos
def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(2, -2) == 0.25
    assert calc.potencia(1e5, 2) == 1e10  

# Testes com entradas inválidas
def test_entradas_invalidas(calc):
    with pytest.raises(TypeError):
        calc.adicionar("dois", 2)
    with pytest.raises(TypeError):
        calc.subtrair(None, 5)
    with pytest.raises(TypeError):
        calc.multiplicar(3, "três")
    with pytest.raises(TypeError):
        calc.dividir(10, "zero")
    with pytest.raises(TypeError):
        calc.potencia("dez", 2)
    with pytest.raises(TypeError):
        calc.fatorial("cinco")
