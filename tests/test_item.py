"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


# test method init
def test_init(item1):
    """Тестирует метод init."""
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


# test method calculate_total_price
def test_calculate_total_price(item1):
    """Тестирует метод calculate_total_price."""
    assert item1.calculate_total_price() == 200000


# test method apply_discount
def test_apply_discount(item1):
    """Тестирует метод apply_discount."""

    def test_apply_discount(item1):
        Item.pay_rate = 0.8
        assert item1.apply_discount() == None
        assert item1.price == 8000
    # assert item1.price() == None


# test hw2: instantiate_from_csv

def test_len_name_setter(item1):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'


def test_instantiate_from_csv(item1):
    """Тестирует метод instantiate_from_csv."""
    assert len(item1.name) == 8


# test hw2: string_to_number
def test_string_to_number(item1):
    """Тестирует метод string_to_number."""
    assert item1.string_to_number("10000") == 10000
    assert item1.string_to_number("2.034") == 2

