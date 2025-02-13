from typing import Callable

SaludoFuncion = Callable[[], str]

def saludar() -> str:
    return "¡Hola!"

mi_saludo: SaludoFuncion = saludar

print(mi_saludo())