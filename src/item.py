import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", "{self.price}", "{self.quantity}")'

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """Возвращает наименование товара (Getter)"""
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, filepath='items.csv'):
        goods = []
        with open(filepath, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name, price, quantity = row['name'], row['price'], row['quantity']
                item = cls(name, price, quantity)
                goods.append(item)
        return goods

    @staticmethod
    def string_to_number(num):
        return int(num)
