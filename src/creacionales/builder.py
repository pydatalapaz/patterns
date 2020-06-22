import requests

class ApiRestBuilder:
    def __init__(self, url: str):
        self._url = url
        self._version = 'v1'

    def setVersion(self, version):
        self._version = version
        return self
    
    def setMethod(self, method):
        self._method = method
        return self

    def setResource(self, resource):
        self._resource = resource
        return self

    def setHeaders(self, headers):
        self._headers = headers
        return self

    def build(self, body):
        url = f'{self._url}/api/{self._version}/{self._resource}'
        method_to_execute = getattr(requests, self._method, None)

        if method_to_execute is None:
            return None
        
        return method_to_execute(url, body, self._headers)