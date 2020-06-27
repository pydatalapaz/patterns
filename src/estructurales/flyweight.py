class Imagen: # Flyweight
    def __init__(self, url: str):
        self._url = url

    def mostrar(self, alto: int, ancho: int):
        print(f'<img src={self._url} a={alto} an={ancho} />')

class _ImagenFactory:
    def __init__(self):
        self._repo = {}

    def get_imagen(self, url) -> Imagen:
        if url in self._repo.keys():
            return self._repo[url]
        
        nueva_imagen = Imagen(url)
        self._repo[url] = nueva_imagen
        return nueva_imagen

instance = None

def ImagenFactory() -> _ImagenFactory:
    global instance
    if instance is None:
        instance = _ImagenFactory()
    return instance