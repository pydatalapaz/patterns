from typing import List

class Empleado:
    def __init__(self, name: str):
        self._nombre = name

    def notificar(self):
        print(f'{self._nombre} Notificado')

class JefeUnidad(Empleado):
    pass

class Area(Empleado):
    def __init__(self, empleado: Empleado):
        self._empleados: List[Empleado] = [empleado]

    def notificar(self):
        for _ in self._empleados:
            _.notificar()

    def agregar(self, empleado: Empleado):
        self._empleados.append(empleado)