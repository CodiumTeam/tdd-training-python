import abc


class DrinkMaker(abc.ABC):
    def serve_drink(self, command: str) -> None:
        pass
