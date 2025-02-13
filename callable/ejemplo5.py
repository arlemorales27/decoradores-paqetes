from typing import Callable


class Procesador:
    def __init__(self) -> None:
        self.transformacion: Callable[[str], str] = str.upper

    def cambiar_transformacion(self, nueva_func: Callable[[str], str]) -> None:
        self.transformacion = nueva_func

    def procesar(self, texto: str) -> str:
        return self.transformacion(texto)


# Uso
proc = Procesador()
print(proc.procesar("hola"))  # "HOLA"

# Cambiamos la transformación
proc.cambiar_transformacion(str.lower)
print(proc.procesar("HOLA"))
