import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
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
        try:
            with open(filepath, newline='', encoding='windows-1252') as f:
                reader = csv.DictReader(f)
                goods = []
                for row in reader:
                    if len(row) == 3 and ('name' in reader.fieldnames and 'price' in reader.fieldnames
                                          and 'quantity' in reader.fieldnames):
                        item = cls(row['name'], row['price'], row['quantity'])
                        goods.append(item)
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print(f'Отсутствует файл {filepath}')
        except InstantiateCSVError:
            print(f'Файл {filepath} поврежден')
        else:
            return goods

    @staticmethod
    def string_to_number(num):
        return int(num)


if __name__ == '__main__':
    # test1 Рабочий файл
    item = Item.instantiate_from_csv('items.csv')
    item1 = item[0]
    assert item1.price == 100

    # test2 Сломанный файл
    item_broke = Item.instantiate_from_csv('broke_items.csv')
    # Файл broke_items.csv поврежден

    # test3 Отсутствует файл
    item_not_found = Item.instantiate_from_csv('fff')
    # Отсутствует файл fff
