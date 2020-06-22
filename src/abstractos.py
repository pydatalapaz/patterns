import abc
import uuid

class Entidad(abc.ABC):
    def __init__(self):
        self._id: str = str(uuid.uuid4())

    @property
    def id(self):
        return self._id

class Usuario(Entidad):
    def __init__(self, nombre: str):
        super().__init__()
        self._nombre = nombre
    
    @property
    def nombre(self) -> str:
        return self._nombre

class Rol(Entidad):
    def __init__(self, nombre: str):
        super().__init__()
        self._nombre = nombre


class Factura(Entidad):
    pass


class UsuarioSA(Usuario):
    pass


# usu = Usuario(1)
usu = Entidad()