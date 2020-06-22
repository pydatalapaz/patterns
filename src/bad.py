import json
from typing import List
from abstractos import Factura, Usuario
import abc
import csv

def parse_cvs(path: str) -> List[Usuario]:
    csvfile = open('src/db.txt', 'r')
    data = csv.DictReader(csvfile)
    return data

def parse_json(path: str) -> List[Factura]:
    facturas = json.loads(open('src/facturas.json', 'r').read())
    return facturas

def search_facturas(facturas: List[Factura], user_id: str) -> List[Factura]:
    return list(filter(lambda x: str(x['user']) == user_id, facturas))


class Descuento(abc.ABC):
    @abc.abstractmethod
    def calcular_descuento(self) -> str:
        pass

class PythonDescuento(Descuento):
    def calcular_descuento(self) -> str:
        return 0.5

class PhpDescuento(Descuento):
    def calcular_descuento(self) -> str:
        return 0.01

class FacturaFactory:
    def __init__(self, usuario, facturas, calculador: Descuento):
        self._usuario_id = usuario['id']
        self._lang = usuario['language']
        self._facturas = search_facturas(facturas, self._usuario_id)
        self._calculador = calculador

    @property
    def descuento(self):
        return self._calculador(self._lang)


def imprimir_factura(calculador_descuentos: Descuento):
    data = parse_cvs('src/db.txt')
    facturas = parse_json('src/facturas.json')

    usuarios = [FacturaFactory(x, facturas, calculador_descuentos) for x in data]
    print(usuarios)

imprimir_factura(PythonDescuento())
imprimir_factura(PhpDescuento())