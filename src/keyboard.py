from src.item import Item


class MixinKeyboardLanguage:
    """Класс-миксин для хранения и изменения раскладки клавиатуры"""
    def __init__(self, language='EN'):
        """Инициализируем класс MixinKeyboardLanguage"""
        self.__language = language

    @property
    def language(self):
        """Геттер language"""
        return self.__language

    def change_lang(self):
        """Метод для смены раскладки языка"""
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinKeyboardLanguage):
    """Класс для товара Клавиатура, этот класс наследуется от Item"""
    def __str__(self):
        return super().__str__()
