from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """ Инициализирует класс Phone"""
        self.__number_of_sim = number_of_sim
        super().__init__(name, price, quantity)

    @property
    def number_of_sim(self):
        """Геттер метода number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        """Сеттер метода number_of_sim"""
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = value

    def __repr__(self):
        data = super().__repr__()
        return data.replace(')', f', {self.__number_of_sim})')
