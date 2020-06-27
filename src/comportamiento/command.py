from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self): # deshacer
        pass

    def retry(self):
        pass

class Api: # Reviser
    def send(self):
        pass

class CrearCuentaCommand(BaseCommand):
    def __init__(self, cuenta, api):
        self._cuenta = cuenta
        self._api = api

    def execute(self):
        self._api.send()
        print('[CC] -> Creando una cuenta')

    def undo(self):
        print('[CC] -> Deshaciendo: Creando una cuenta')


class EliminacionCuentaCommand(BaseCommand):
    def execute(self):
        print('[EC] -> Eliminado una cuenta')

    def undo(self):
        print('[EC] -> Deshaciendo: Eliminado una cuenta')


class Application: # Invoker
    def __init__(self):
        self._command_history = []

    def add_btn_click(self):
        add_cmd = CrearCuentaCommand('a', Api())
        add_cmd.execute()
        self._command_history.append(add_cmd)

    def delete_btn_click(self):
        del_cmd = EliminacionCuentaCommand()
        del_cmd.execute()
        self._command_history.append(del_cmd)
        
    def undo(self):
        last_cmd = self._command_history.pop()
        last_cmd.undo()

    def retry(self):
        last_cmd = self._command_history.pop()
        last_cmd.retry()