import pytest
from src.keyboard import Keyboard

@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test_init_keyboard(keyboard):
    """Тест, что в ините EN по умолчанию"""
    assert keyboard.language == 'EN'
    assert keyboard.language != 'RU'
    assert keyboard.language != 'CH'

def test_setter_language(keyboard):
    """Тест сеттер self.__language"""
    with pytest.raises(AttributeError):
        keyboard.language = 'RU'

def test_change_language(keyboard):
    """Тест для метода смены раскладки языка"""
    assert keyboard.language == 'EN'
    assert keyboard.language != 'RU'
    assert keyboard.language != 'CH'

