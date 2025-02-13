from typing import Callable, Any

# Función que acepta cualquier número de argumentos
#*args permite pasar un número variable de argumentos posicionales.
# El asterisco * desempaqueta una tupla de argumentos.
#**kwargs (Argumentos Nombrados)
#**kwargs permite pasar un número variable de argumentos nombrados (keyword arguments).
#El doble asterisco ** desempaqueta un diccionario de argumentos.
FuncionGenerica = Callable[..., Any]

def procesar(*args: Any, **kwargs: Any) -> Any:
    return len(args) + len(kwargs)

mi_funcion: FuncionGenerica = procesar

print(mi_funcion(1,2,4,9, nombre="Juan"))