from src.item import Item
import pytest
import os


@pytest.fixture()
def item1():
    return Item("Телефон", 10000, 20)


def test_name_setter(item1):
    item1.name = "Смартфон"
    assert item1.name == "Смартфон"


def test_name_setter_value_error(item1):
    item1.name = "СуперСмартфон"
    assert item1.name == "Телефон"


def test_instantiate_from_csv():
    filename = os.path.join(os.path.dirname(__file__), '..', 'src', 'items.csv')
    items = Item.instantiate_from_csv(filename)
    assert len(items) == 5
    item1 = items[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number(5.0) == 5
    assert Item.string_to_number(5.5) == 5
