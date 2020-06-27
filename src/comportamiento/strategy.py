from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, value: str) -> str:
        pass

class JsonParser(Parser):
    def parse(self, value: str) -> str:
        return 'json-' + value

class XMLParser(Parser):
    def parse(self, value: str) -> str:
        return 'XML-' + value

class NullParser(Parser):
    def parse(self, value: str) -> str:
        return value

class ApiDemo:
    def __init__(self, parser: Parser=NullParser()):
        self._parser = parser

    def send(self, data: str):
        print(self._parser.parse(data))