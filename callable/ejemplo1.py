from typing import Callable

# Definimos un tipo de función que toma dos enteros y retorna un entero
OperacionMatematica = Callable[[int, int], int]

def suma(a: int, b: int) -> int:
    return a + b

# Declaramos una variable que almacenará una función
operacion: OperacionMatematica = suma

# Uso
resultado = operacion(5, 3)  # 8

print(resultado)
