from abc import ABC, abstractmethod

class Heroe(ABC):
    @abstractmethod
    def fuerza(self):
        pass

    @abstractmethod
    def agilidad(self):
        pass

    @abstractmethod
    def inteligencia(self):
        pass

class Pudge(Heroe):
    def fuerza(self):
        return 18

    def agilidad(self):
        return 10

    def inteligencia(self):
        return 8


class Item(Heroe, ABC):
    def __init__(self, heroe: Heroe):
        self._heroe = heroe

    def fuerza(self):
        return self._heroe.fuerza()

    def agilidad(self):
        return self._heroe.agilidad()

    def inteligencia(self):
        return self._heroe.inteligencia()

class CinturonFuerza(Item):
    def fuerza(self):
        return self._heroe.fuerza() + 8

class CapaMago(Item):
    def inteligencia(self):
        return self._heroe.inteligencia() + 10