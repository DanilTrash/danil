from abc import ABC, abstractmethod
from typing import Optional, Tuple, TypeVar

T = TypeVar("T")


class Handler(ABC):
    def __init__(self, successor: Optional[T] = None):
        self.successor = successor

    def handle(self, request: int) -> None:
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request: int) -> Optional[bool]:
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):

    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True


class ConcreteHandler1(Handler):

    start, end = 10, 20

    def check_range(self, request: int) -> Optional[bool]:
        if self.start <= request < self.end:
            print(f"request {request} handled in handler 1")
            return True


class ConcreteHandler2(Handler):

    def check_range(self, request: int) -> Optional[bool]:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled in handler 2")
            return True

    @staticmethod
    def get_interval_from_db() -> Tuple[int, int]:
        return (20, 30)


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        print(f"end of chain, no handler for {request}")
        return False


def main():
    h0 = ConcreteHandler0()
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2()
    h_fb = FallbackHandler()
    h0.successor = h1
    h1.successor = h2
    h2.successor = h_fb
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    for request in requests:
        h0.handle(request)


if __name__ == "__main__":
    main()
