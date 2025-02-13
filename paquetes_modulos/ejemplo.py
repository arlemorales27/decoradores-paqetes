# Importar módulos específicos
from mipaquete.operaciones import operaciones
print(operaciones.sumar(5, 3))  # 8

# Importar funciones específicas
from mipaquete.operaciones.geometria import area_circulo
print(area_circulo(2))  # 12.566370614359172

# Importar versión del paquete
from mipaquete import VERSION
print(VERSION)  # 1.0.0
