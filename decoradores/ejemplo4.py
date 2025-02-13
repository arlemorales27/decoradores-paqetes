from typing import Optional


class Rectangulo:
    def __init__(self, ancho: float, alto: float) -> None:
        self._ancho: float = ancho
        self._alto: float = alto
        self._area: Optional[float] = None

    @property
    def area(self) -> float:
        """
        Calcula y retorna el área del rectángulo.

        Returns:
            float: El área del rectángulo
        """
        # Cacheamos el resultado para evitar recálculos innecesarios
        if self._area is None:
            self._area = self._ancho * self._alto
        return self._area

    @property
    def ancho(self) -> float:
        """
        Obtiene el ancho del rectángulo.

        Returns:
            float: El ancho del rectángulo
        """
        return self._ancho

    @ancho.setter
    def ancho(self, valor: float) -> None:
        """
        Establece el ancho del rectángulo.

        Args:
            valor: El nuevo ancho

        Raises:
            ValueError: Si el valor es negativo o cero
        """
        if valor > 0:
            self._ancho = valor
            self._area = None  # Invalidamos el cache
        else:
            raise ValueError("El ancho debe ser positivo")
