from abc import ABC, abstractmethod

class BaseObserver(ABC):
    @abstractmethod
    def notify(self, state: str):
        pass

class ObserverOne(BaseObserver):
    def notify(self, state: str):
        print(f'O1 -> {state}')

class ObserverTwo(BaseObserver):
    def notify(self, state: str):
        print(f'O2 -> {state}')

class Subject:
    def __init__(self):
        self._obervadores_registrados = []
        self._state: str

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, newState):
        self._state = newState
        self._notify()

    def add_observer(self, observer: BaseObserver):
        self._obervadores_registrados.append(observer)

    def remove_observadores(self, observer):
        pass
    
    def _notify(self):
        for _ in self._obervadores_registrados:
            _.notify(self.state)
