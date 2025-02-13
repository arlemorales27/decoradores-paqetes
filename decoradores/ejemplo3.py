from typing import Type, Optional


class Matematicas:
    valor_pi: float = 3.14159

    @staticmethod
    def es_par(numero: int) -> bool:
        return numero % 2 == 0

    def __init__(self, valor: int) -> None:
        self.valor: int = valor


print(Matematicas.es_par(3))
