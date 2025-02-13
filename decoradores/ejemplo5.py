from typing import Callable, TypeVar, Any

T = TypeVar('T')  # Tipo genérico para la clase


def agregar_saludo(cls: type[T]) -> type[T]:
    """
    Decorador que agrega un método de saludo a cualquier clase.
    """

    def saludar(self) -> str:
        return f"¡Hola! Soy una instancia de {self.__class__.__name__}"

    cls.saludar = saludar  # Añade el método a la clase
    return cls


# Uso del decorador
@agregar_saludo
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def obtener_info(self) -> str:
        return f"Me llamo {self.nombre} y tengo {self.edad} años"


# Ejemplo de uso
persona = Persona("Ana", 25)
print(persona.saludar())  # Imprime: ¡Hola! Soy una instancia de Persona
print(persona.obtener_info())  # Imprime: Me llamo Ana y tengo 25 años