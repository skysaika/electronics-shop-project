import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)


def test_phone_init(phone1):
    """Тестирую инит"""
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_add_classes(phone1, item1):
    """Тестирую сложение классов"""
    assert phone1.price + item1.price == 130_000
    assert item1.quantity + phone1.quantity == 25


def test_phone_repr(phone1):
    """Тест repr"""
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_failing_add_classes(phone1, item1):
    """Тест должен показать ошибку при сложении не phone1 или не item1"""
    with pytest.raises(TypeError):
        phone1 + 25

def test_number_of_sim(phone1, item1):
    """Тестируем количество сим-карт"""
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

