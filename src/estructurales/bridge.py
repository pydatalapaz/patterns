from abc import ABC, abstractmethod

class Switch(ABC): # Abstractor
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Electronico(ABC): # Implementor
    @abstractmethod
    def encender_impl(self):
        pass

    @abstractmethod
    def apagar_impl(self):
        pass

class HomeSwitch(Switch):
    def __init__(self, electrico: Electronico):
        self._electronico = electrico

    def encender(self):
        self._electronico.encender_impl()

    def apagar(self):
        self._electronico.apagar_impl()

class Foco(Electronico):
    def apagar_impl(self):
        print('Se apago el foco')

    def encender_impl(self):
        print('Se encendio el foco')

class Computador(Electronico):
    def apagar_impl(self):
        print('Se apagara la pc en 8 s')

    def encender_impl(self):
        print('Se encendio la')