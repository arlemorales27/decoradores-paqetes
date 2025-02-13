from typing import Callable


class Calculadora:
    def __init__(self, operacion: Callable[[float, float], float]) -> None:
        self.operacion = operacion

    def calcular(self, x: float, y: float) -> float:
        return self.operacion(x, y)


# Funciones que podemos usar
def sumar(a: float, b: float) -> float:
    return a + b


def multiplicar(a: float, b: float) -> float:
    return a * b


# Uso
calc_suma = Calculadora(sumar)
calc_mult = Calculadora(multiplicar)

print(calc_suma.calcular(5.0, 3.0))  # 8.0
print(calc_mult.calcular(5.0, 3.0))  # 15.0
