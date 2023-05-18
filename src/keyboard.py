from src.item import Item


class MixinLog:

    def __init__(self):
        self.__keylang = "EN"

    @property
    def keylang(self):
        return self.__keylang

    def change_lang(self):
        if self.__keylang == "RU":
            self.__keylang = "EN"
        else:
            self.__keylang = "RU"
        return self


class Keyboard(Item, MixinLog):
    def __init__(self, __name: str, price: float, quantity: int) -> None:
        super().__init__(__name, price, quantity)
        MixinLog.__init__(self)

