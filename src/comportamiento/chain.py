from abc import ABC, abstractmethod

class Request:
    def __init__(self):
        self._body = ""
    
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body

class RequestHandler(ABC):
    def __init__(self):
        self._handler_anterior = None

    @abstractmethod
    def handle_request(self, request: Request):
        pass

    def set_anterior(self, anterior):
        self._handler_anterior = anterior

class MidddlewareHandler(RequestHandler):
    def handle_request(self, request: Request):
        if self._handler_anterior is not None:
            request = self._handler_anterior.handle_request(request)
        print(f'M -> {request.body}')
        request.body = 'from middleware'
        return request

class ControllerHandler(RequestHandler):
    def handle_request(self, request: Request):
        if self._handler_anterior is not None:
            request = self._handler_anterior.handle_request(request)
        print(f'C -> {request.body}')
        return request