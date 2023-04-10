"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item('Смартфон', 10000, 20)


def test_instantiate_from_csv(item1):
    """Тестирует метод instantiate_from_csv."""
    Item.instantiate_from_csv(CSV_FILE='./src/items.csv')
    assert len(Item.all[0].name) == 8
    assert len(Item.all) == 6


def test_init(item1):
    """Тестирует метод init."""
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_repr(item1):
    """Тестирует метод repr."""
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    """Тестирует метод str."""
    assert str(item1) == "Смартфон"


def test_calculate_total_price(item1):
    """Тестирует метод calculate_total_price."""
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    """Тестирует метод apply_discount."""
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000
    # assert item1.price() == None


def test_len_name_setter(item1):
    """Тестирует сеттер  self.__name."""
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'


def test_change_name_setter(item1):
    """Тест смены названия"""
    item1.name = "Тарелка"
    assert item1.name == "Тарелка"


def test_string_to_number(item1):
    """Тестирует метод string_to_number."""
    assert item1.string_to_number("10000") == 10000
    assert item1.string_to_number("2.034") == 2


def test_positive_add(item1):
    """Тестирует сложение классов"""
    test_item1 = Item('Смартфон', 1000, 3)
    assert item1 + test_item1 == 23


def test_error_add(item1):
    """Тестирует ошибку сложения"""
    with pytest.raises(TypeError):
        result = item1 + 10


def test_get_data_from_csv(item1):
    """Тест получения данных из csv"""
    Item.instantiate_from_csv(CSV_FILE='../src/items.csv')


def test_init_instantiate_csv_error(args=None):
    """Тест ошибки инита"""
    with pytest.raises(TypeError):
        args[0] = "Файл item.csv поврежден"
