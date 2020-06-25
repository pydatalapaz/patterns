from abc import ABC, abstractmethod

class ApiClient(ABC):
    @abstractmethod
    def version(self):
        pass

class ApiRestClient(ApiClient):
    def version(self):
        return 'V1Rest'

class SoapClient(ApiClient):
    def version(self):
        return 'V2Soap'

class WCFClient:
    def get_version(self):
        return 'V3 WCF'

class WCFClientAdapter(ApiClient):
    def __init__(self, wcf: WCFClient):
        self._wcf = wcf

    def version(self):
        return self._wcf.get_version()