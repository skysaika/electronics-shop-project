import csv

from src.settings import take_from_csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def name(self) -> str:
        """Геттер для названия товара."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Сеттер для названия товара."""
        self.__name = name
        if len(self.__name) > 10:
            raise ValueError("Название должно быть не более 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализация класса Item из файла csv."""
        cls.all = []
        for data in take_from_csv():
            cls(*data)

    @staticmethod
    def take_from_csv() -> list:
        """Получение данных из файла csv"""
        data_list = []
        with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
            data_csv = csv.reader(csvfile, delimiter=',')
            for elem in data_csv:
                if elem[0] == 'name':
                    continue
                else:
                    data_list.append(elem)
            return data_list

    @staticmethod
    def string_to_number(number: str) -> int:
        """Преобразование строки в число."""
        return int(number.split(".")[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
