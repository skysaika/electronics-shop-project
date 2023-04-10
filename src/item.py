import csv


class InstantiateCSVError(Exception):
    """Класс выявления ошибки в случае, если в файле отсутствуют необходимые поля"""

    def __init__(self, *args):
        """Конструктор класса InstantiateCSVError"""
        self.msg = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        """Возврат строкового представления класса InstantiateCSVError"""
        return self.msg


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self) -> str:
        """Геттер для названия товара."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Сеттер для названия товара."""
        if len(name) > 10:
            raise ValueError("Название должно быть не более 10 символов.")
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls, CSV_FILE='../src/items.csv'):
        """Метод открытия файла с исключениями"""
        try:
            with open(CSV_FILE, encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if any(row.get(value) is None for value in ['name', 'price', 'quantity']):
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    cls.all.append((row['name'], float(row['price']), int(row['quantity'])))
        except FileNotFoundError:
            print("Отсутствует файл item.csv")

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

    def __add__(self, other: 'Item'):
        """Складывает экземпляры класса """
        if not isinstance(other, Item):
            raise TypeError('Нельзя складывать разные классы.')
        return self.quantity + other.quantity
