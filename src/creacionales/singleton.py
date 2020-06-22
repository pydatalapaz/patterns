class _DBConn:
    pass

_instance: _DBConn = None 

def DBConn():
    global _instance
    if _instance is None:
        _instance = _DBConn()
    return _instance


class _UserConfig:
    def __init__(self):
        print('Creando instancia de User Config')
        self._idioma = 'es'
        self._theme = 'black'

    @property
    def theme(self):
        return self._theme

_userConfigInstance: _UserConfig = None

def UserConfig():
    global _userConfigInstance
    if _userConfigInstance is None:
        _userConfigInstance = _UserConfig()
    return _userConfigInstance

