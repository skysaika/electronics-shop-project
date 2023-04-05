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

    @language.setter
    def language(self, language):
        """Сеттер language"""
        if language not in self.__language:
            raise AttributeError('Язык должен быть EN или RU')

    def change_lang(self):
        """Метод для смены раскладки языка"""
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'
        return self


class Keyboard(Item, MixinKeyboardLanguage):
    """Класс для товара Клавиатура, этот класс наследуется от Item"""
    def __str__(self):
        return super().__str__()
