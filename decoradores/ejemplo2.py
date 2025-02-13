from typing import Callable, TypeVar, Any

T = TypeVar('T')  # Tipo genérico para mayor flexibilidad


def operacion(x: float,
              y: float,
              func: Callable[[float, float], float]) -> float:
    """
    Ejecuta una operación matemática usando la función proporcionada.

    Args:
        x: Primer número
        y: Segundo número
        func: Función que realizará la operación

    Returns:
        float: Resultado de la operación
    """
    return func(x, y)


def suma(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def multiplicacion(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


# Ejemplos de uso:
resultado_suma = operacion(5.0, 3.0, suma)  # 8.0
resultado_mult = operacion(5.0, 3.0, multiplicacion)  # 15.0
