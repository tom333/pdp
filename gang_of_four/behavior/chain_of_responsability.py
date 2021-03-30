from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Permet d'enchainer les déclarations
        # handler1.set_next(handler2).set_next(handler3)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Handler1(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Type1":
            return "%s handled by Handler1" % request
        else:
            return super().handle(request)


class Handler2(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Type2":
            return "%s handled by Handler2" % request
        else:
            return super().handle(request)


class Handler3(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Type3":
            return "%s handled by Handler3" % request
        else:
            return super().handle(request)


if __name__ == "__main__":
    handler1 = Handler1()
    handler2 = Handler2()
    handler3 = Handler3()

    handler1.set_next(handler2).set_next(handler3)

    for type_name in ["Type2", "Type1", "Type3"]:
        res = handler1.handle(type_name)
        print(res)
