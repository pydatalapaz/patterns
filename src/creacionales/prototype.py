import uuid
from typing import List

class Usuario:
    def __init__(self, name: str, permissions: List[str]):
        self._id: str = str(uuid.uuid4())
        self._name = name
        self._permissions: List[str] = permissions

    def clone(self):
        self._id: str = str(uuid.uuid4())
        return self

class UsuarioAdministrador(Usuario):
    def __init__(self, name: str):
        super().__init__(name, ['Puede Crear Post', 'Puede Eliminar Posts'])

class UsuarioNormal(Usuario):
    def __init__(self, name: str):
        super().__init__(name, [])

class UsuarioSuperAdministrador(Usuario):
    def __init__(self, name: str):
        super().__init__(name, ['A', '..', 'Z'])